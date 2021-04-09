from PySide6.QtWidgets import QMainWindow, QApplication, QButtonGroup, QFileSystemModel, QFileDialog
from PySide6.QtCore import QDir
from studioui import Ui_MainWindow


from custom_logging import *
from composition import *
import sys
import os
import pickle
import time

# Represents values in UI comboboxes, used by update keysig methods
NOTES = ["A", "B", "C", "D", "E", "F", "G"]
ACCIDENTALS = ["♮", "♯", "♭"]
SCALES = ["major", "minor", "harmonic", "melodic"]

# Dict holding named sets of duration weights
#(6, 1), (4, 6), (3, 5), (2, 16), (1.5, 3), (1, 26), (.75, 3), (.5, 20), (.375, 4), (.25, 6), (.1875, 0), (.125, 2), (.0625, 1)
PRESET_WEIGHTS = {
}


class Studio(QMainWindow):
	def __init__(self):
		super(Studio, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.configuration = {} # always represents active ui
		self.init_user_input_vars()
		self.init_ui()

	def init_ui(self):

		self.ui.dialog_anchor.setStyleSheet("QWidget {color: rgb(137, 137, 206)}")

		self.ui.nav_group = QButtonGroup()
		self.ui.nav_group.addButton(self.ui.nav_configure)
		self.ui.nav_group.addButton(self.ui.nav_write)

		self.ui.ranges_group = QButtonGroup()
		self.ui.ranges_group.addButton(self.ui.sharp_ranges)
		self.ui.ranges_group.addButton(self.ui.flat_ranges)
		self.ui.sharp_ranges.setCheckable(True)
		self.ui.flat_ranges.setCheckable(True)
		self.ui.sharp_ranges.setChecked(True)

		# Signal Connections
		# connected function is an update function
		# update functions are always called in response to user input updates
		# to modify class attributes and call other methods to update other display areas when needed
		# some updates use other functions to handle the attribute change

		self.ui.nav_group.buttonClicked.connect(self.navigate)

		self.ui.save.clicked.connect(self.save_configuration)
		self.ui.load.clicked.connect(self.load_configuration)

		# Configure
		self.ui.measures.textEdited.connect(self.update_measures)

		self.ui.timesig_num.textEdited.connect(self.update_timesig)
		self.ui.timesig_den.textEdited.connect(self.update_timesig)

		self.ui.keysig_note.currentTextChanged.connect(self.update_keysig_note)
		self.ui.keysig_acc.currentTextChanged.connect(self.update_keysig_acc)
		self.ui.keysig_scale.currentTextChanged.connect(self.update_keysig_scale)

		self.ui.ranges_group.buttonClicked.connect(self.update_ranges_mode)
		self.ui.lh_range1_slider.valueChanged.connect(self.update_lh_range1)
		self.ui.lh_range2_slider.valueChanged.connect(self.update_lh_range2)
		self.ui.rh_range1_slider.valueChanged.connect(self.update_rh_range1)
		self.ui.rh_range2_slider.valueChanged.connect(self.update_rh_range2)

		self.ui.whole_weight_slider.valueChanged.connect(self.update_whole_weight)
		self.ui.half_weight_slider.valueChanged.connect(self.update_half_weight)
		self.ui.quarter_weight_slider.valueChanged.connect(self.update_quarter_weight)
		self.ui.eighth_weight_slider.valueChanged.connect(self.update_eighth_weight)
		self.ui.sixteenth_weight_slider.valueChanged.connect(self.update_sixteenth_weight)

		# Write
		self.ui.song_name.textEdited.connect(self.update_song_name)
		self.ui.song_folder.clicked.connect(self.select_song_folder)

		self.ui.pdf.stateChanged.connect(self.update_pdf)
		self.ui.midi.stateChanged.connect(self.update_midi)

		self.ui.compose.clicked.connect(self.compose)


	def init_user_input_vars(self):
		# User input vars are Studio level variables reflecting the current state of ui input widgets
		self.song_name = "<unnamed>"
		self.song_folder = os.getcwd()+"/output"

		self.ranges_mode = "♯"
		self.ui.lh_range1_slider.setSliderPosition(0)
		self.ui.lh_range2_slider.setSliderPosition(39)
		self.ui.rh_range1_slider.setSliderPosition(39)
		self.ui.rh_range2_slider.setSliderPosition(87)
		self.configuration["rh_range2"] = self.ui.rh_range2_slider.value()
		self.configuration["lh_range2"] = self.ui.lh_range2_slider.value()

		self.configuration["weights"] = {}
		self.configuration["weights"]["whole"] = self.ui.whole_weight_slider.value()
		self.configuration["weights"]["half"] = self.ui.half_weight_slider.value()
		self.configuration["weights"]["quarter"] = self.ui.quarter_weight_slider.value()
		self.configuration["weights"]["eighth"] = self.ui.eighth_weight_slider.value()
		self.configuration["weights"]["sixteenth"] = self.ui.sixteenth_weight_slider.value()

		self.update_all()


	# runs every update method
	def update_all(self):
		self.update_measures()
		self.update_timesig()
		self.update_keysig_note()
		self.update_keysig_acc()
		self.update_keysig_scale()
		self.update_song_name()
		self.update_all_ranges()
		self.update_all_weights()
		self.update_pdf()
		self.update_midi()

	def navigate(self, button):
		if button == self.ui.nav_configure:
			self.ui.configure.raise_()
		elif button == self.ui.nav_write:
			self.ui.write.raise_()

	# Compose button should only be pushable with a valid folder selected
	def compose(self):
		Composition(self.song_folder, self.song_name +".ly", self.collect_song_parameters())

	# assembles and returns a dictionary representing new song's musical parameters derived from user inputs
	def collect_song_parameters(self):
		rules = {}
		rules['measures'] = self.configuration['measures']
		rules['timesig'] = self.configuration['timesig']
		rules['key'] = self.assemble_key()
		rules['key_scale'] = self.configuration['keysig_scale']
		rules['lh_ranges'] = [self.lh_range1_lynotation, self.lh_range2_lynotation]
		rules['rh_ranges'] = [self.rh_range1_lynotation, self.rh_range2_lynotation]
		rules['pdf'] = self.configuration['pdf']
		rules['midi'] = self.configuration['midi']

		return rules

	def update_song_name(self):
		self.song_name = self.ui.song_name.text()

	def update_measures(self):
		if self.ui.measures.text():
			self.configuration['measures'] = int(self.ui.measures.text())

	def update_timesig(self):
		if self.ui.timesig_num.text() and self.ui.timesig_den.text(): # for when user clears field
			self.configuration['timesig'] = (int(self.ui.timesig_num.text()), int(self.ui.timesig_den.text()))
		
	def update_keysig_note(self):   # change to cycler
		self.configuration["keysig_note"] = self.ui.keysig_note.currentText()

	def update_keysig_scale(self):
		self.configuration["keysig_scale"] = self.ui.keysig_scale.currentText()

	def update_keysig_acc(self):
		self.configuration["keysig_acc"] = self.ui.keysig_acc.currentText()

		# change range mode as needed
		if self.configuration["keysig_acc"] == "♯":
			self.ranges_mode = "♯"
			self.ui.sharp_ranges.setChecked(True)
			self.ui.sharp_ranges.setEnabled(False)
			self.ui.flat_ranges.setEnabled(False)
			self.update_all_ranges()
		elif self.configuration["keysig_acc"] == "♭":
			self.ranges_mode = "♭"
			self.ui.flat_ranges.setChecked(True)
			self.ui.sharp_ranges.setEnabled(False)
			self.ui.flat_ranges.setEnabled(False)
			self.update_all_ranges()
		else:
			self.ui.sharp_ranges.setEnabled(True)
			self.ui.flat_ranges.setEnabled(True)

	def update_ranges_mode(self, button):
		if button == self.ui.sharp_ranges:
			self.ranges_mode = "♯"
			self.update_all_ranges()
		else:
			self.ranges_mode = "♭"
			self.update_all_ranges()

	def update_lh_range1(self):
		self.configuration["lh_range1"] = self.ui.lh_range1_slider.value()
		lynotation = ""

		if self.ranges_mode == "♯":
			lynotation = pitchesre.SHARP_LIST[self.configuration["lh_range1"]]
		elif self.ranges_mode == "♭":
			lynotation = pitchesre.FLAT_LIST[self.configuration["lh_range1"]]

		self.lh_range1_lynotation = lynotation
		self.lh_range1_numbered = self.lynotation_to_numbered(lynotation)

		#update labels
		self.ui.lh_range1_label.setText(self.lh_range1_numbered)
		self.ui.lh_range1_header_label.setText(self.lh_range1_numbered)
		self._update_lh_span()

	def update_lh_range2(self):
		self.configuration["lh_range2"] = self.ui.lh_range2_slider.value()
		lynotation = ""

		if self.ranges_mode == "♯":
			lynotation = pitchesre.SHARP_LIST[self.configuration["lh_range2"]]
		elif self.ranges_mode == "♭":
			lynotation = pitchesre.FLAT_LIST[self.configuration["lh_range2"]]

		self.lh_range2_lynotation = lynotation
		self.lh_range2_numbered = self.lynotation_to_numbered(lynotation)

		#update labels
		self.ui.lh_range2_label.setText(self.lh_range2_numbered)
		self.ui.lh_range2_header_label.setText(self.lh_range2_numbered)
		self._update_lh_span()

	def _update_lh_span(self):
		self.lh_span = self.configuration["lh_range2"] - self.configuration["lh_range1"]
		self.ui.lh_span.setText(str(abs(self.lh_span)))

	def update_rh_range1(self):
		self.configuration["rh_range1"] = self.ui.rh_range1_slider.value()
		lynotation = ""

		if self.ranges_mode == "♯":
			lynotation = pitchesre.SHARP_LIST[self.configuration["rh_range1"]]
		elif self.ranges_mode == "♭":
			lynotation = pitchesre.FLAT_LIST[self.configuration["rh_range1"]]

		self.rh_range1_lynotation = lynotation
		self.rh_range1_numbered = self.lynotation_to_numbered(lynotation)

		#update labels
		self.ui.rh_range1_label.setText(self.rh_range1_numbered)
		self.ui.rh_range1_header_label.setText(self.rh_range1_numbered)
		self._update_rh_span()

	def update_rh_range2(self):
		self.configuration["rh_range2"] = self.ui.rh_range2_slider.value()
		lynotation = ""

		if self.ranges_mode == "♯":
			lynotation = pitchesre.SHARP_LIST[self.configuration["rh_range2"]]
		elif self.ranges_mode == "♭":
			lynotation = pitchesre.FLAT_LIST[self.configuration["rh_range2"]]

		self.rh_range2_lynotation = lynotation
		self.rh_range2_numbered = self.lynotation_to_numbered(lynotation)

		#update labels
		self.ui.rh_range2_label.setText(self.rh_range2_numbered)
		self.ui.rh_range2_header_label.setText(self.rh_range2_numbered)

		self._update_rh_span()

	def update_all_ranges(self):
		self.update_lh_range1()
		self.update_lh_range2()
		self.update_rh_range1()
		self.update_rh_range2()

	def _update_rh_span(self):
		self.rh_span = self.configuration["rh_range2"] - self.configuration["rh_range1"]
		self.ui.rh_span.setText(str(abs(self.rh_span)))

	def update_all_weights(self):
		self.update_whole_weight()
		self.update_half_weight()
		self.update_quarter_weight()
		self.update_eighth_weight()
		self.update_sixteenth_weight()

	def update_whole_weight(self):
		self.configuration["weights"]["whole"] = self.ui.whole_weight_slider.value()
		self.ui.whole_weight_value.setText(str(self.configuration["weights"]["whole"]+1))

	def update_half_weight(self):
		self.configuration["weights"]["half"] = self.ui.half_weight_slider.value()
		self.ui.half_weight_value.setText(str(self.configuration["weights"]["half"]+1))

	def update_quarter_weight(self):
		self.configuration["weights"]["quarter"] = self.ui.quarter_weight_slider.value()
		self.ui.quarter_weight_value.setText(str(self.configuration["weights"]["quarter"]+1))

	def update_eighth_weight(self):
		self.configuration["weights"]["eighth"] = self.ui.eighth_weight_slider.value()
		self.ui.eighth_weight_value.setText(str(self.configuration["weights"]["eighth"]+1))

	def update_sixteenth_weight(self):
		self.configuration["weights"]["sixteenth"] = self.ui.sixteenth_weight_slider.value()
		self.ui.sixteenth_weight_value.setText(str(self.configuration["weights"]["sixteenth"]+1))

	def update_pdf(self):
		self.configuration["pdf"] = self.ui.pdf.isChecked()

	def update_midi(self):
		self.configuration["midi"] = self.ui.pdf.isChecked()


	# converts lyform notation to numbered notation for display purposes for range sliders
	def lynotation_to_numbered(self, lynotation):

		clef = 3
		numbered = [lynotation[0]]

		for c in lynotation:
			if c == ",":
				clef -= 1
			elif c == "'":
				clef += 1
		if clef != 0:
			numbered.append(str(clef))
			
		if "is" in lynotation:
			numbered.append("♯")
		elif "es" in lynotation:
			numbered.append("♭")

		return "".join(numbered)

	def assemble_key(self):
		if self.configuration["keysig_acc"] == "♯":
			return f"{self.configuration['keysig_note'].lower()}is"
		elif self.configuration["keysig_acc"] == "♭":
			return f"{self.configuration['keysig_note'].lower()}es"
		else:
			return self.configuration["keysig_note"].lower()


	# Configurations
	def save_configuration(self):
		save_dialog = QFileDialog.getSaveFileName(self.ui.dialog_anchor, "Save Configuration", f"{os.getcwd()}/configurations", ".cf", options=QFileDialog.DontUseNativeDialog)
		if save_dialog[0]:
			configuration_filename = ""
			if save_dialog[0][-3:] != '.cf':
				configuration_filename = save_dialog[0]+save_dialog[1]
			self._write_configuration(configuration_filename)

	def _write_configuration(self, configuration_filename):
		pickle.dump(self.configuration, open(configuration_filename, 'wb'))

	def load_configuration(self):
		if configuration_filename := QFileDialog.getOpenFileName(self.ui.dialog_anchor, "Load Configuration", f"{os.getcwd()}/configurations", "*.cf", options=QFileDialog.DontUseNativeDialog)[0]:

			self.configuration = pickle.load(open(configuration_filename, "rb"))
			log_debug(f"before applying self.configuration: {self.configuration}")
			self.apply_configuration()

	def apply_configuration(self):
		print('applying config')
		self.ui.measures.setText(str(self.configuration['measures']))
		self.ui.timesig_num.setText(str(self.configuration['timesig'][0]))
		self.ui.timesig_den.setText(str(self.configuration['timesig'][1]))

		# combobox inputs convert back to related index from stored string value
		self.ui.keysig_note.setCurrentIndex(self.index_from_note(self.configuration["keysig_note"]))
		self.ui.keysig_acc.setCurrentIndex(self.index_from_acc(self.configuration["keysig_acc"]))
		self.ui.keysig_scale.setCurrentIndex(self.index_from_scale(self.configuration["keysig_scale"]))

		self.ui.rh_range1_slider.setSliderPosition(self.configuration["rh_range1"])
		self.ui.rh_range2_slider.setSliderPosition(self.configuration["rh_range2"])
		self.ui.lh_range1_slider.setSliderPosition(self.configuration["lh_range1"])
		self.ui.lh_range2_slider.setSliderPosition(self.configuration["lh_range2"])

		self.update_all() # probably the way to do it 

	def index_from_note(self, note):
		for i in range(len(NOTES)):
			if NOTES[i] == note:
				return i

	def index_from_acc(self, acc):
		for i in range(len(ACCIDENTALS)):
			if ACCIDENTALS[i] == acc:
				return i

	def index_from_scale(self, scale):
		for i in range(len(SCALES)):
			if SCALES[i] == scale:
				return i

	# Songs
	def select_song_folder(self):
		if directory := QFileDialog.getExistingDirectory(self.ui.dialog_anchor, "Select Folder", os.getcwd()+"/output", options=QFileDialog.ShowDirsOnly|QFileDialog.DontUseNativeDialog):
			direct = QDir(os.getcwd()).relativeFilePath(directory)
			self.song_folder = direct
			self.update_song_filename()

	def update_song_filename(self):
		print(self.song_filename())
		self.ui.song_filename_label.setText(self.song_filename())

	def song_filename(self):
		return f"{self.song_folder}/{self.song_name}.ly"

app = QApplication(sys.argv)
app_window = Studio()

app_window.show()
sys.exit(app.exec_())