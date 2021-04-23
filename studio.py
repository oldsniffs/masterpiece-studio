import sys
import os
import pickle
from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QSlider, QLabel, QDial, QAbstractSlider
from PySide6.QtCore import QFile, QPropertyAnimation, QEasingCurve
from studio_ui import Ui_MainWindow

from default_settings import *
from custom_logging import *
from composition import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.animation = None

        self.configuration = self.startup_configuration()
        self.active_style = self.configuration.active_segment['style']  # self.load_configuration must redo this

        self.init_ui()
        self.refresh_full_ui()

    # Configuration ////////////////
    def startup_configuration(self):
        # Could be extended to recall settings @ last close
        # or call it refresh_configuration
        return Configuration()


    def clear_configuration(self):
        self.configuration = Configuration()
        self.active_style = self.configuration.active_segment['style']

    def init_ui(self):

        # HOW TO FIND A CHILD
        print(self.ui.weights_arch_widget.findChild(QSlider, "half_prime_slider"))

        # Close "Configure" sub-menu
        self.ui.styleNav.setMaximumHeight(0)
        # Clear placeholder texts
        self.clear_top_bar_info()

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

        # Style ////////////////////////////

        # Rhythm ///
        # Timesig
        self.ui.timesig_num.textEdited.connect(self.update_timesig_num)
        self.ui.timesig_den.textEdited.connect(self.update_timesig_den)

        # Assign same signal connections for like widgets
        for name, widget in self.ui.__dict__.items():

            # QAbstractSlider
            if isinstance(widget, QAbstractSlider):
                # weights
                if "prime_slider" in name or "pair_slider" in name:
                    widget.actionTriggered.connect(self.update_weight)

                if "longevity_dial" in name or "spawn_dial" in name or "gravity_dial" in name or "velocity_dial" in name:
                    widget.actionTriggered.connect(self.update_anchor)


        # Pitch ///
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
        # weights
        for weight in self.active_style['weights'].keys():
            if "prime" in weight or "pair" in weight:
                self.refresh_weight(weight)
            if "length" in weight:
                # handle length weights
                pass

        # anchors
        for anchor in self.active_style['anchors'].keys():
            self.refresh_anchor(anchor)

        # range bounds
        self.refresh_bounds()

    # Rhythm
    # timesig
    def update_timesig_num(self):
        self.active_style['timesig'][0] = int(self.ui.timesig_num.text())

    def update_timesig_den(self):
        # Check for valid entry
        try:
            self.active_style['timesig'][1] = int(self.ui.timesig_den())
        except ValueError:
            self.ui.timesig_valid_indicator

        # if self.timesig_validation(self.active_style['timesig']) == True:
        #     self.ui.timesig_indicator = True
            #  Animation
            #  bad = red
            #  good = turn green & fade

    # Weights
    def update_weight(self, action):
        log_debug(f"updating weight from slider: {self.sender().objectName()}")
        weight = self.sender().objectName()[:-7]
        self.active_style['weights'][weight] = self.sender().sliderPosition()
        self.refresh_weight(weight)

    def refresh_weight(self, weight):  # weight format: "whole_prime""
        log_debug(f"refreshing weight: {weight}")
        self.ui.weights_arch_widget.findChild(QSlider, weight+"_slider").setValue(self.active_style['weights'][weight])
        self.ui.weights_arch_widget.findChild(QLabel, weight+"_display").setText(str(self.active_style['weights'][weight]))

    # Anchors
    def update_anchor(self, action):
        log_debug(f"updating anchor from dial: {self.sender().objectName()}")
        anchor = self.sender().objectName()[:-5]
        self.active_style['anchors'][anchor] = self.sender().sliderPosition()
        self.refresh_anchor(anchor)

    def refresh_anchor(self, anchor):
        log_debug(f"refreshing anchor: {anchor}")
        self.ui.anchors_arch_widget.findChild(QDial, anchor+"_dial").setValue(self.active_style['anchors'][anchor])
        self.ui.anchors_arch_widget.findChild(QLabel, anchor+"_display").setText(str(self.active_style['anchors'][anchor]))

    # Pitch /////
    # Range Bounds
    def update_left_lower_bound(self):
        log_debug(f"updating left_lower")
        # Check that bounds don't cross
        if self.ui.left_lower_slider.sliderPosition() > self.ui.left_upper_slider.sliderPosition():
            self.active_style['bounds']['left_lower'] = self.ui.left_upper_slider.sliderPosition()
        else:
            self.active_style['bounds']['left_lower'] = self.ui.left_lower_slider.sliderPosition()
        self.refresh_left_lower_bound('left_lower')

    def refresh_left_lower_bound(self):
        log_debug(f"refreshing left lower")
        self.ui.left_lower_slider.setValue(self.active_style['bounds']['left_lower'])
        self.ui.left_lower_display.setText(self.slider_index_to_spn(self.active_style['bounds']['left_lower']))

    def update_left_upper_bound(self):
        log_debug(f"updating left upper")
        if self.ui.left_upper_slider.sliderPosition() < self.ui.left_lower_slider.sliderPosition():
            self.active_style['bounds']['left_upper'] = self.ui.left_lower_slider.sliderPosition()
        else:
            self.active_style['bounds']['left_upper'] = self.ui.left_upper_slider.sliderPosition()
        self.refresh_left_upper_bound()

    def refresh_left_upper_bound(self):
        log_debug(f"refreshing left upper")
        self.ui.left_upper_slider.setValue(self.active_style['bounds']['left_upper'])
        self.ui.left_upper_display.setText(self.slider_index_to_spn(self.active_style['bounds']['left_upper']))

    def update_right_lower_bound(self):
        log_debug(f"updating right_lower")
        # A check could occur here to stop bound values from passing their complement (use closest allowed value)
        if self.ui.right_lower_slider.sliderPosition() > self.ui.right_upper_slider.sliderPosition():
            self.active_style['bounds']['right_lower'] = self.ui.right_upper_slider.sliderPosition()
        else:
            self.active_style['bounds']['right_lower'] = self.ui.right_lower_slider.sliderPosition()
        self.refresh_right_lower_bound()

    def refresh_right_lower_bound(self):
        log_debug(f"refreshing right lower")
        self.ui.right_lower_slider.setValue(self.active_style['bounds']['right_lower'])
        self.ui.right_lower_display.setText(self.slider_index_to_spn(self.active_style['bounds']['right_lower']))

    def update_right_upper_bound(self):
        log_debug(f"updating right upper")
        if self.ui.right_upper_slider.sliderPosition() < self.ui.right_lower_slider.sliderPosition():
            self.active_style['bounds']['right_upper'] = self.ui.right_lower_slider.sliderPosition()
        else:
            self.active_style['bounds']['right_upper'] = self.ui.right_upper_slider.sliderPosition()
        self.refresh_right_upper_bound()

    def refresh_right_upper_bound(self):
        log_debug(f"refreshing right upper")
        self.ui.right_upper_slider.setValue(self.active_style['bounds']['right_upper'])
        self.ui.right_upper_display.setText(self.slider_index_to_spn(self.active_style['bounds']['right_upper']))

    def update_ranges_mode(self, btn):
        if btn == self.ui.sharp_ranges:
            self.active_style['ranges_mode'] = "♯"
            log_debug(f"ranges mode now sharp")
        else:
            self.active_style['ranges_mode'] = "♭"
            log_debug(f"ranges mode now flat")
        self.refresh_bounds()

    def refresh_bounds(self):
        self.refresh_left_lower_bound()
        self.refresh_left_upper_bound()
        self.refresh_right_lower_bound()
        self.refresh_right_upper_bound()

    # Structure
    def update_length(self):
        self.configuration.active_segment['length'] = int(self.ui.length_entry.text())
        # somewhere, a check for validity
        self.refresh_length()

    # as widget is a lineEdit, this function makes the border green or red based on validity
    def refresh_length(self):
        pass

    # UI Utility ////////////////////////////////////////////////////////////////////////////////// UI Utility

    def clear_top_bar_info(self):
        self.ui.active_configuration_display.setText("")
        self.ui.active_style_display.setText("")
    # Save and Load Configurations //////

    def slider_index_to_spn(self, index):
        index += 9  # fills 0 octave
        octave = int(index / 12)
        if self.active_style['ranges_mode'] == "♯":
            pitch = SHARP_OCTAVE[index % 12]
        else:
            pitch = FLAT_OCTAVE[index % 12]
        return f"{octave}{pitch}"


# Holds data that always reflects current state of the UI, via it's active_segment, updated as user modifies inputs
# Has methods to convert raw user input to a Composition-ready data structure
# Configuration segments store user data, Composition-ready segments are outputted from them
class Configuration:
    def __init__(self):
        self.name = "New Configuration"
        self.segments = [{'length': DEFAULT_LENGTH, 'style': STANDARD_STYLE}]
        self.active_segment = self.segments[0]

    # convert to Composition-ready
    def prepare_for_composition(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
