import sys
import pickle
from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QSlider, QLabel, QDial, QAbstractSlider, QComboBox, QFileDialog, QPushButton
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QDir
from PySide6.QtGui import QIcon
from studio_ui import Ui_MainWindow

from default_settings import *
from composer import *
from lily import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.animation = None
        self.composition = None
        self.configuration = None
        self.active_style = None
        self.load_configuration(Configuration("unnamed"))

        self.init_ui()
        # self.refresh_full_ui()

    # Configuration ////////////////
    def load_configuration(self, configuration):
        self.configuration = configuration
        self.active_style = self.configuration.active_segment['style']
        self.ui.topBar_active_configuration_display.setText(self.configuration.name)
        self.ui.topBar_active_style_display.setText(self.active_style['name'])
        self.ui.compose_active_configuration_display.setText(self.configuration.name)
        self.update_weight_total("prime")
        self.update_weight_total("pair")
        self.refresh_full_ui()

    def init_ui(self):


        # Icon
        self.setWindowIcon(QIcon("data/images/icon.png"))
        # HOW TO FIND A CHILD
        print(self.ui.weights_arch_widget.findChild(QSlider, "half_prime_slider"))

        # Close "Configure" sub-menu
        self.ui.styleNav.setMaximumHeight(0)
        # Clear placeholder text

        # Compose
        self.ui.save_config_btn.clicked.connect(self.save_configuration_dialog)
        self.ui.loaf_config_btn.clicked.connect(self.load_configuration_dialog)
        self.ui.compose_btn.clicked.connect(self.compose)

        self.ui.composition_name_entry.textChanged.connect(self.update_composition_name)

        # Navigation
        self.ui.main_nav_group = QButtonGroup()
        self.ui.main_nav_group.setExclusive(True)
        self.ui.main_nav_group.buttonClicked.connect(self.navigate)
        self.ui.main_nav_group.addButton(self.ui.structure_nav_btn)
        self.ui.structure_nav_btn.setCheckable(True)
        self.ui.main_nav_group.addButton(self.ui.style_nav_btn)
        self.ui.style_nav_btn.setCheckable(True)
        self.ui.main_nav_group.addButton(self.ui.compose_nav_btn)
        self.ui.compose_nav_btn.setCheckable(True)
        self.navigate(self.ui.compose_nav_btn)

        self.ui.style_nav_group = QButtonGroup()
        self.ui.style_nav_group.setExclusive(True)
        self.ui.style_nav_group.buttonClicked.connect(self.navigate_style)
        self.ui.style_nav_group.addButton(self.ui.pitch_nav_btn)
        self.ui.pitch_nav_btn.setCheckable(True)
        self.ui.style_nav_group.addButton(self.ui.rhythm_nav_btn)
        self.ui.rhythm_nav_btn.setCheckable(True)
        self.ui.style_nav_group.addButton(self.ui.aharmony_nav_btn)
        self.ui.aharmony_nav_btn.setCheckable(True)
        # Start style nav at rhythm page
        self.ui.style_stack.setCurrentWidget(self.ui.rhythm_page)
        self.ui.rhythm_nav_btn.setChecked(True)

        # Structure ////////////////////////
        self.ui.length_entry.textChanged.connect(self.update_length)
        # Style ////////////////////////////

        # Rhythm ///
        # Timesig
        self.ui.timesig_den.setCurrentIndex(1)
        self.ui.timesig_num.textEdited.connect(self.update_timesig_num)
        self.ui.timesig_den.currentIndexChanged.connect(self.update_timesig_den)
        self.ui.bpm_entry.textEdited.connect(self.update_bpm)

        # Beats
        self.beat_buttons = []
        self.ui.beats_widget.resizeEvent(self.refresh_beats())

        # Assign same signal connections for like widgets
        for name, widget in self.ui.__dict__.items():

            # QAbstractSlider
            if isinstance(widget, QAbstractSlider):
                # weights
                if "prime_slider" in name or "pair_slider" in name:
                    widget.actionTriggered.connect(self.update_weight)

                if "longevity_dial" in name or "spawn_dial" in name or "gravity_dial" in name or "velocity_dial" in name:
                    widget.actionTriggered.connect(self.update_anchor)

        self.ui.snap_slider.actionTriggered.connect(self.update_snap)
        self.ui.rest_slider.actionTriggered.connect(self.update_rest)

        # Pitch ///
        # Keysig
        self.ui.atonal_check.stateChanged.connect(self.update_atonal)
        self.ui.keysig_pitch_combo.currentIndexChanged.connect(self.update_keysig_component)
        self.ui.keysig_acc_combo.currentIndexChanged.connect(self.update_keysig_component)
        self.ui.keysig_scale_combo.currentIndexChanged.connect(self.update_keysig_component)

        # Ranges
        self.ui.ranges_group = QButtonGroup()
        self.ui.ranges_group.buttonClicked.connect(self.update_ranges_mode)
        self.ui.ranges_group.addButton(self.ui.sharp_ranges)
        self.ui.ranges_group.addButton(self.ui.flat_ranges)
        self.ui.sharp_ranges.setCheckable(True)
        self.ui.flat_ranges.setCheckable(True)
        self.ui.sharp_ranges.setChecked(True)

        self.ui.left_lower_slider.actionTriggered.connect(self.update_left_lower_bound)
        self.ui.left_upper_slider.actionTriggered.connect(self.update_left_upper_bound)
        self.ui.right_lower_slider.actionTriggered.connect(self.update_right_lower_bound)
        self.ui.right_upper_slider.actionTriggered.connect(self.update_right_upper_bound)

    # Override UI virtual functions

    def resizeEvent(self, event):
        self.refresh_beats()

    # Navigation //////////////////////////////////////////////////////////////////////////////////// Navigation

    def navigate(self, calling_btn):
        self.toggle_style_nav(calling_btn)
        if calling_btn == self.ui.style_nav_btn:
            self.ui.content_stack.setCurrentWidget(self.ui.style_page)
        elif calling_btn == self.ui.compose_nav_btn:
            self.ui.content_stack.setCurrentWidget(self.ui.compose_page)
        elif calling_btn == self.ui.structure_nav_btn:
            self.ui.content_stack.setCurrentWidget(self.ui.structure_page)

    def toggle_style_nav(self, calling_btn):
        if self.ui.styleNav.maximumHeight() == 0 and calling_btn == self.ui.style_nav_btn:
            self.open_style_nav()

        elif self.ui.styleNav.maximumHeight() == 160 and calling_btn != self.ui.style_nav_btn:
            self.close_style_nav()

    def close_style_nav(self):
        self.animation = QPropertyAnimation(self.ui.styleNav, b'maximumHeight')
        self.animation.setDuration(500)
        self.animation.setStartValue(160)
        self.animation.setEndValue(0)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def open_style_nav(self):
        self.animation = QPropertyAnimation(self.ui.styleNav, b'maximumHeight')
        self.animation.setDuration(350)
        self.animation.setStartValue(0)
        self.animation.setEndValue(160)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def navigate_style(self, calling_btn):
        if calling_btn == self.ui.pitch_nav_btn:
            self.ui.style_stack.setCurrentWidget(self.ui.pitch_page)
        elif calling_btn == self.ui.rhythm_nav_btn:
            self.ui.style_stack.setCurrentWidget(self.ui.rhythm_page)
        elif calling_btn == self.ui.aharmony_nav_btn:
            self.ui.style_stack.setCurrentWidget(self.ui.aharmony_page)

        calling_btn.setChecked(True)

    # Update and Refresh //////////////////////////////////////////////////////////////////////// Update and Refresh

    def refresh_full_ui(self):
        # Top bar
        self.refresh_configuration_name()

        # Compose
        self.refresh_composition_name()

        # Structure
        self.refresh_length()

        # Style

        # rhythm
        self.refresh_timesig_num()
        self.refresh_timesig_den()
        self.refresh_bpm()
        self.refresh_snap()

        for weight in self.active_style['weights'].keys():
            if "prime" in weight or "pair" in weight:
                self.refresh_weight(weight)
            if "length" in weight:
                # handle length weights
                pass
        self.refresh_prime_total()
        self.refresh_pair_total()

        # pitch
        self.refresh_bounds()
        self.refresh_keysig()

        for anchor in self.active_style['anchors'].keys():
            self.refresh_anchor(anchor)

    # Top Bar ////

    def update_configuration_name(self, text):
        self.configuration.name = text
        self.refresh_configuration_name()

    def refresh_configuration_name(self):
        self.ui.topBar_active_configuration_display.setText(self.configuration.name)

    # Compose
    def update_composition_name(self, text):
        self.configuration.composition_name = text

    def refresh_composition_name(self):
        self.ui.composition_name_entry.setText(self.configuration.composition_name)

    # Structure
    def refresh_style_color(self, style):
        pass

    # Rhythm /////

    # Timesig
    # UI will accept bad input, but will disable compose button until input is valid
    def update_timesig_num(self):
        log_debug(f"updating timesig_num")
        if self.ui.timesig_num.text() != "":
            self.active_style['timesig_num'] = int(self.ui.timesig_num.text())
        self.refresh_beats()

    def refresh_timesig_num(self):
        log_debug(f"refreshing timesig_num")
        self.ui.timesig_num.setText(str(self.active_style['timesig_num']))

    def update_timesig_den(self):
        log_debug(f"updating timesig_den")
        self.active_style['timesig_den'] = int(self.ui.timesig_den.currentText())

    def refresh_timesig_den(self):
        log_debug(f"refresh timesig_den")
        self.ui.timesig_den.setCurrentText(str(self.active_style['timesig_den']))

    # could have buttons premade standing by, or create and delete each timesig_num change
    def refresh_beats(self):
        log_debug(f"refreshing beats")
        # remove or add buttons
        beat_count = self.active_style['timesig_num']

        button_count = len(self.beat_buttons)
        balance = self.active_style['timesig_num'] - button_count
        if balance != 0:
            if balance > 0:
                log_info(f"{balance} beat buttons must be added")
                for b in range(balance):
                    button = QPushButton(self.ui.beats_widget)
                    button.setText(f"{str(button_count+b+1)}\n")
                    # It seems I will have to calculate the geometry for each button configuration, as qt is placing them all at 0,0 inside the parent by default
                    button.setVisible(True)
                    button.setMaximumWidth(100)
                    button.setCheckable(True) # Could do a programmed tri-state button for hierarchy
                    button.clicked.connect(self.update_division_beats)
                    self.beat_buttons.append(button)

            elif balance < 0:
                log_info(f"{balance*-1} beat buttons must be removed")
                for b in range(balance*-1):
                    self.beat_buttons[-1].setParent(None)
                    self.beat_buttons.pop()

            # For duple time


        log_debug(self.beat_buttons)

        total_width = self.ui.beats_widget.width()
        button_count = len(self.beat_buttons)
        button_width = int(total_width / button_count)-10
        for b in range(button_count):
            self.beat_buttons[b].setGeometry((button_width+4)*b, 0, button_width, 40)
        # self.refresh_division_beats()

    # A beat button has been toggled
    def update_division_beats(self, isChecked):
        log_info(f"updating division_beats")
        beat = int(self.sender().text())
        log_debug(f'beat {beat} is {isChecked}')
        if isChecked:
            self.active_style['division_beats'].append(beat)
        else:
            self.active_style['division_beats'].remove(beat)

    def refresh_division_display(self):
        pass

    def refresh_beat_widget(self):
        # division_beats color: color: rgb(161, 239, 119)
        pass

    def _remove_beat_button(self, number):
        pass

    def _add_beat_button(self, number):
        button = QPushButton(parent=self.ui.beats_widget)
        # text
        button.setText(number)
        # connect
        button.clicked.connect(self.update_division_beats)

        self.beat_buttons.append(button)

    def update_beat_divisons(self):
        beat = self.sender().text()


    # Bpm
    def update_bpm(self, text):
        if self.ui.timesig_num.text() != "":
            self.active_style['bpm'] = int(text)

    def refresh_bpm(self):
        self.ui.bpm_entry.setText(str(self.active_style['bpm']))

    # Weights
    def update_weight(self, action):
        log_debug(f"updating weight from slider: {self.sender().objectName()}")
        weight = self.sender().objectName()[:-7]
        self.active_style['weights'][weight] = self.sender().sliderPosition()
        self.update_weight_total(weight)
        self.refresh_weight(weight)

    def update_weight_total(self, weight):
        log_debug(f"updating total after change to {weight}")
        if "prime" in weight:
            total = 0
            for key, value in self.active_style['weights'].items():
                if "prime" in key:
                    total += value
            self.active_style['prime_total'] = total
            self.refresh_prime_total()
        if "pair" in weight:
            total = 0
            for key, value in self.active_style['weights'].items():
                if "pair" in key:
                    total += value
            self.active_style['pair_total'] = total
            self.refresh_pair_total()

    def refresh_weight(self, weight):  # weight format: "whole_prime""
        log_debug(f"refreshing weight: {weight}")
        self.ui.weights_arch_widget.findChild(QSlider, weight+"_slider").setValue(self.active_style['weights'][weight])
        self.ui.weights_arch_widget.findChild(QLabel, weight+"_display").setText(str(self.active_style['weights'][weight]))

    def refresh_prime_total(self):
        self.ui.prime_total_display.setText(str(self.active_style['prime_total']))

    def refresh_pair_total(self):
        self.ui.pair_total_display.setText(str(self.active_style['pair_total']))
    # \\ Snap

    def update_snap(self, action):
        log_debug(f"updating snap")
        self.active_style['snap'] = self.ui.snap_slider.sliderPosition()
        self.refresh_snap()

    def refresh_snap(self):
        log_debug(f"refreshing snap")
        self.ui.snap_slider.setValue(self.active_style['snap'])
        self.ui.snap_display.setText(str(self.active_style['snap']))

    # \\ Rest Conversion

    def update_rest(self, action):
        log_debug(f"updating rest")
        self.active_style['rest'] = self.ui.rest_slider.sliderPosition()
        self.refresh_rest()

    def refresh_rest(self):
        log_debug(f"refreshing rest")
        self.ui.rest_slider.setValue(self.active_style['rest'])
        self.ui.rest_display.setText(str(self.active_style['rest']))

    #
    # Pitch /////

    # Anchors
    def update_anchor(self):
        log_debug(f"updating anchor from dial: {self.sender().objectName()}")
        anchor_setting = self.sender().objectName()[:-5]
        self.active_style['anchors'][anchor_setting] = self.sender().sliderPosition()
        self.refresh_anchor(anchor_setting)

    def refresh_anchor(self, anchor_setting):
        log_debug(f"refreshing anchor: {anchor_setting}")
        self.ui.anchors_arch_widget.findChild(QDial, anchor_setting+"_dial").setValue(self.active_style['anchors'][anchor_setting])
        self.ui.anchors_arch_widget.findChild(QLabel, anchor_setting+"_display").setText(str(self.active_style['anchors'][anchor_setting]))

    # Keysig
    # Updates for combo boxes using parallel lists
    def update_atonal(self, whoknows):
        log_debug(f"THIS is whoknows: {whoknows}")
        # whoknows is 0 or 2, could be used for conditional
        if self.ui.atonal_check.isChecked():
            self.active_style['keysig_atonal'] = True
        else:
            self.active_style['keysig_atonal'] = False

        self.refresh_atonal()

    def refresh_atonal(self):
        log_debug(f"refreshing atonal")
        if self.active_style['keysig_atonal']:
            self.ui.keysig_component_bar.setEnabled(False)
        else:
            self.ui.keysig_component_bar.setEnabled(True)

    def update_keysig_component(self):
        log_debug(f"updating keysig from: {self.sender().objectName()}")
        component = self.sender().objectName()[:-6]
        self.active_style[component] = self.sender().currentText()
        log_debug(self.active_style[component])

    def refresh_keysig_component(self, component):
        log_debug(f"refreshing keysig  component: {component}")
        self.ui.keysig_arch_widget.findChild(QComboBox, component+"_combo").setCurrentText(self.active_style[component])

    def refresh_keysig(self):
        self.refresh_keysig_component('keysig_pitch')
        self.refresh_keysig_component('keysig_acc')
        self.refresh_keysig_component('keysig_scale')
        self.refresh_atonal()

    # Range Bounds
    def update_left_lower_bound(self):
        log_debug(f"updating left_lower")
        # Check that bounds don't cross
        if self.ui.left_lower_slider.sliderPosition() > self.ui.left_upper_slider.sliderPosition():
            self.active_style['bounds']['left_lower'] = self.ui.left_upper_slider.sliderPosition()
            self.active_style['bounds']['left_lower_spn'] = index_to_spn(self.active_style,
                                                                         self.active_style['bounds']['left_lower'])
        else:
            self.active_style['bounds']['left_lower'] = self.ui.left_lower_slider.sliderPosition()
            self.active_style['bounds']['left_lower_spn'] = index_to_spn(self.active_style,
                                                                         self.active_style['bounds']['left_lower'])
        self.refresh_left_lower_bound()

    def refresh_left_lower_bound(self):
        log_debug(f"refreshing left lower")
        self.ui.left_lower_slider.setValue(self.active_style['bounds']['left_lower'])
        self.ui.left_lower_display.setText(self.active_style['bounds']['left_lower_spn'])

    def update_left_upper_bound(self):
        log_debug(f"updating left upper")
        if self.ui.left_upper_slider.sliderPosition() < self.ui.left_lower_slider.sliderPosition():
            self.active_style['bounds']['left_upper'] = self.ui.left_lower_slider.sliderPosition()
            self.active_style['bounds']['left_upper_spn'] = index_to_spn(self.active_style,
                                                                         self.active_style['bounds']['left_upper'])
        else:
            self.active_style['bounds']['left_upper'] = self.ui.left_upper_slider.sliderPosition()
            self.active_style['bounds']['left_upper_spn'] = index_to_spn(self.active_style,
                                                                         self.active_style['bounds']['left_upper'])
        self.refresh_left_upper_bound()

    def refresh_left_upper_bound(self):
        log_debug(f"refreshing left upper")
        self.ui.left_upper_slider.setValue(self.active_style['bounds']['left_upper'])
        self.ui.left_upper_display.setText(self.active_style['bounds']['left_upper_spn'])

    def update_right_lower_bound(self):
        log_debug(f"updating right_lower")
        # A check could occur here to stop bound values from passing their complement (use closest allowed value)
        if self.ui.right_lower_slider.sliderPosition() > self.ui.right_upper_slider.sliderPosition():
            self.active_style['bounds']['right_lower'] = self.ui.right_upper_slider.sliderPosition()
            self.active_style['bounds']['right_lower_spn'] = index_to_spn(self.active_style,
                                                                          self.active_style['bounds']['right_lower'])
        else:
            self.active_style['bounds']['right_lower'] = self.ui.right_lower_slider.sliderPosition()
            self.active_style['bounds']['right_lower_spn'] = index_to_spn(self.active_style,
                                                                          self.active_style['bounds']['right_lower'])
        self.refresh_right_lower_bound()

    def refresh_right_lower_bound(self):
        log_debug(f"refreshing right lower")
        self.ui.right_lower_slider.setValue(self.active_style['bounds']['right_lower'])
        self.ui.right_lower_display.setText(self.active_style['bounds']['right_lower_spn'])

    def update_right_upper_bound(self):
        log_debug(f"updating right upper")
        if self.ui.right_upper_slider.sliderPosition() < self.ui.right_lower_slider.sliderPosition():
            self.active_style['bounds']['right_upper'] = self.ui.right_lower_slider.sliderPosition()
            self.active_style['bounds']['right_upper_spn'] = index_to_spn(self.active_style,
                                                                          self.active_style['bounds']['right_upper'])
        else:
            self.active_style['bounds']['right_upper'] = self.ui.right_upper_slider.sliderPosition()
            self.active_style['bounds']['right_upper_spn'] = index_to_spn(self.active_style,
                                                                          self.active_style['bounds']['right_upper'])

        self.refresh_right_upper_bound()

    def refresh_right_upper_bound(self):
        log_debug(f"refreshing right upper")
        self.ui.right_upper_slider.setValue(self.active_style['bounds']['right_upper'])
        self.ui.right_upper_display.setText(self.active_style['bounds']['right_upper_spn'])

    def update_ranges_mode(self, btn):
        if btn == self.ui.sharp_ranges:
            self.active_style['ranges_mode'] = "♯"
            self.active_style['spn_list'] = SHARP_SPN_LIST
            log_debug(f"ranges mode now sharp")
        else:
            self.active_style['ranges_mode'] = "♭"
            self.active_style['spn_list'] = FLAT_SPN_LIST
            log_debug(f"ranges mode now flat")
        self.refresh_bounds()

    def refresh_bounds(self):
        self.refresh_left_lower_bound()
        self.refresh_left_upper_bound()
        self.refresh_right_lower_bound()
        self.refresh_right_upper_bound()

    # Structure
    def update_length(self):
        log_debug(f"updating length")
        if self.ui.length_entry.text() != "":
            self.configuration.active_segment['length'] = int(self.ui.length_entry.text())

    def refresh_length(self):
        log_debug(f"refreshing length")
        self.ui.length_entry.setText(str(self.configuration.active_segment['length']))

    # UI Utility ////////////////////////////////////////////////////////////////////////////////// UI Utility

    def index_to_ly(self, index, mode):
        if mode == "♯":
            return SHARP_PITCHES[index]
        else:
            return FLAT_PITCHES[index]

    # Save and Load Configurations //////

    def save_configuration_dialog(self):
        save_dialog = QFileDialog.getSaveFileName(self.ui.dialog_anchor, "Save Configuration",
                                                  f"{os.getcwd()}", "*.cf",
                                                  options=QFileDialog.DontUseNativeDialog)
        if save_dialog[0]:
            configuration_filename = ""
            if save_dialog[0][-3:] != '.cf':
                configuration_filename = save_dialog[0] + '.cf'
            saved_as = configuration_filename[len(os.getcwd()):]
            self.update_configuration_name(saved_as)
            self.write_configuration(configuration_filename)

    def write_configuration(self, filename):
        pickle.dump(self.configuration, open(filename, 'wb'))

    def load_configuration_dialog(self):
        filename = QFileDialog.getOpenFileName(self.ui.dialog_anchor, "Load Configuration",
                                               f"{os.getcwd()}/configurations/", "*.cf",
                                               options=QFileDialog.DontUseNativeDialog)[0]
        if filename:
            try:
                self.load_configuration(pickle.load(open(filename, 'rb')))
            except:
                log_info(f"Can not load configuration file: {filename}")

    def save_style_dialog(self):
        save_dialog = QFileDialog


    # Compose ////////////////////////////////////////////////////////////////////////////////////// Compose

    # instantiates Composition
    # writes .ly
    # call lilypond subprocess
    def compose(self):
        self.configuration.finalize_composition_parameters()
        self.composition = Composer(self.configuration)

        log_debug(f"{self.composition.note_tally}")

        if self.configuration.output == "lilypond":
            output = Lily(self.composition)
            output.output()


# Holds data that always reflects current state of the UI, via it's active_segment, updated as user modifies inputs
# Has method finalize_composition_parameters to prepare a Composition-ready data structure
# Configuration segments store user data, Composition-ready segments are outputted from them
class Configuration:
    def __init__(self, name):
        self.name = name
        self.composition_name = "Unnamed Composition"
        self.composition_filepath = ""
        self.composition_filename = ""
        self.composition_cmp_filename = ""
        self.filepath = ""
        self.output = "lilypond"

        self.segments = [{'start': 1, 'stop': 16, 'length': 16, 'style': STANDARD_STYLE, 'measures': []}]

        # Initialize items that usually rely on ui update functions
        self.time_signature = (self.segments[0]['style']['timesig_num'], self.segments[0]['style']['timesig_den'])

        self.segments[0]['style']['bounds']['left_lower_spn'] = index_to_spn(self.segments[0]['style']['ranges_mode'], self.segments[0]['style']['bounds']['left_lower'])
        self.segments[0]['style']['bounds']['left_upper_spn'] = index_to_spn(self.segments[0]['style']['ranges_mode'], self.segments[0]['style']['bounds']['left_upper'])
        self.segments[0]['style']['bounds']['right_lower_spn'] = index_to_spn(self.segments[0]['style']['ranges_mode'], self.segments[0]['style']['bounds']['right_lower'])
        self.segments[0]['style']['bounds']['right_upper_spn'] = index_to_spn(self.segments[0]['style']['ranges_mode'], self.segments[0]['style']['bounds']['right_upper'])

        self.active_segment = self.segments[0]

    # Adds song data at compose time with finalized user input
    def finalize_composition_parameters(self):
        self.finalize_song_info()
        self.finalize_segments()
        self.finalize_composition_filepath()

    def finalize_song_info(self):
        self.keysig_pitch = self.segments[0]['style']['keysig_pitch'].lower()
        scale = self.segments[0]['style']['keysig_scale'].lower()
        for minor_type in ["harmonic", "melodic"]:
            if minor_type in scale:
                scale = minor_type
        self.keysig_scale = scale

    def finalize_segments(self):
        segment_index = 0
        for segment in self.segments:
            segment['index'] = segment_index
            segment['style']['duration_sheet'], segment['style']['note_sheet'], segment['style']['note_beat_values'], segment['style']['note_sheet_ascending'], segment['style']['note_sheet_descending'] = get_sheets(segment['style']['timesig_den'])
            segment['style']['increment'] = self.get_increment(segment['style']['duration_sheet'])
            segment['style']['right_prime_weights'], segment['style']['left_prime_weights'], segment['style']['pair_weights'], segment['style']['length_weights'] = self.get_weight_lists(segment['style']['weights'])
            # Skew weights for left

            # Set up ready-to-use measures list
            segment['measures'] = [{
                'number': measure,
                'style': segment['style'],
                'kites':{"overflow": False},
                'right_durations': [],
                'left_durations':[],
                'right_music':[],
                'left_music':[]
            } for measure in range(segment['start'], segment['stop'])]
            segment_index += 1

    def finalize_composition_filepath(self):
        self.composition_file_namebase = self.composition_name.replace(" ", "_")
        self.composition_filepath = f"{os.getcwd()}/compositions/{self.composition_file_namebase}/"
        self.composition_cmp_filename = f"{self.composition_filepath}/{self.composition_file_namebase}.cmp"
        self.composition_filename = f"{self.composition_filepath}{self.composition_file_namebase}"

    def get_increment(self, prime_durations):
        return prime_durations[6]

    #
    # As per design doc, if notesheet is implemented, this will change
    def get_weight_lists(self, weights):
        prime_weights = [weights['whole_prime'], weights['half_prime'],
                         weights['quarter_prime'], weights['eighth_prime'],
                         weights['sixteenth_prime'], weights['thirtysecond_prime'],
                         weights['sixtyfourth_prime'],
                         weights['dwhole_prime'], weights['dhalf_prime'],
                         weights['dquarter_prime'], weights['deighth_prime'],
                         weights['dsixteenth_prime'], weights['dthirtysecond_prime'],
                         weights['dsixtyfourth_prime']]

        pair_weights = [weights['whole_pair'], weights['half_pair'],
                        weights['quarter_pair'], weights['eighth_pair'],
                        weights['sixteenth_pair'], weights['thirtysecond_pair'],
                        weights['sixtyfourth_pair']]

        length_weights = [weights['eighth_length'], weights['sixteenth_length'],
                          weights['thirtysecond_length'], weights['sixtyfourth_length']]

        return prime_weights, prime_weights, pair_weights, length_weights


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # Create the logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Remove PySide6 (or other) handlers
    for h in logger.handlers:
        logger.removeHandler(h)

    config_log()

    sys.exit(app.exec_())

