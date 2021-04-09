import subprocess
import os

from custom_logging import *
import durationsre
import pitchesre


"""
LY_BLOCKs form a skeleton frame for lywriter notation
"""

LY_BLOCK_1 = """upper = {
  \\clef treble
  \\key c \\major
  \\time 4/4
  
"""

LY_BLOCK_2 = """
}

lower = {
  \\clef bass
  \\key c \\major
  \\time 4/4

"""

LY_BLOCK_3 = """
}

\\score {
  \\new PianoStaff <<
    \\set PianoStaff.instrumentName = #"Piano  "
    \\new Staff = "upper" \\upper
    \\new Staff = "lower" \\lower
  >>
"""


# Builds music from user input and writes files
# constructor calls Rhythm and Notation constructors with user input
# Argument rules: dict of data converted from Studio obj's configuration attribute to be Composition-ready

class Composition:
	def __init__(self, folder, filename, rules):
		self.filepath = folder
		self.filename = filename
		self.__dict__.update(rules)

		self.rhythm = durationsre.Rhythm(self.measure_count, self.timesig)
		self.notation = pitchesre.Notation(self.key, self.key_scale, self.lh_ranges, self.rh_ranges, self.rhythm, None, 1, None)

		self.write_ly(self.lywrite_content())


	def lywrite_content(self):
		rh_ly = self._lywrite_hand(self.notation.left_notation)
		lh_ly = self._lywrite_hand(self.notation.right_notation)
		content = LY_BLOCK_1 + rh_ly + LY_BLOCK_2 + lh_ly + LY_BLOCK_3
		# sort of assuming layout { } means build a pdf to lywriter
		if self.pdf:
			content += """
			\\layout { }"""
		if self.midi:
			content += """
			\\midi { }"""
		content += """
		}"""

		return content

	def _lywrite_hand(self, hand_notation):
		lywritten = ""
		for n in hand_notation:
			if "|" in n:
				print(f"Adding {n}")
				lywritten = lywritten + f'{n} '
			else:
				print(f"Adding {n}")
				lywritten = lywritten + f'{n} '
		return lywritten

	def write_ly(self, content):
		try:
			log_debug(f"os.getcwd(): {os.getcwd()}")
			log_debug(f"self.filepath: {self.filepath}")
			log_debug(f"self.filename: {self.filename}")
			os.mkdir(self.filepath)
		except FileExistsError as e:
			log_warning(e)
		file = open(f"{self.filepath}/{self.filename}", 'w')
		file.write(content)
		file.close()
		log_debug(f"starting lily")
		log_debug(content)
		if self.pdf:
			starting_dir = os.getcwd()
			os.chdir(self.filepath)
			log_debug(f"os.getcwd(): {os.getcwd()} {self.filename}")
			subprocess.call(["lilypond", self.filename])
			os.chdir(starting_dir)
