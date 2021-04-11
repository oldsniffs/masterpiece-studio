import os
import notes

from custom_logging import *


# Builds music from user input and writes files
# Argument song_parameters: dict of data converted from Studio object's configuration attribute to be Composition-ready

class Composition:
	def __init__(self, song_info, style_segments):

		log_header('Composition constructor starting')

		# song-level info
		self.song_info = song_info

		# [(starting measure as integer, musical parameters as dictionary),...]
		self.style_segments = style_segments

		# alt names: music_data, pattern
		# holds full musical pattern as a list of Measure dictionaries
		# instantiate it as a list of empty dictionaries, each being a measure
		self.music = [{} for measure in self.measure_count]

		# generate music by operating on self.music
		self.apply_musical_parameters()
		self.fill_music()

	# copies musical parameters into each measure from self.style_segments
	def apply_musical_parameters(self):
		if len(self.style_segments) == 1:
			for measure in self.music:
				measure.__dict__.update(self.style_segments[0][1])

		else:
			measure = 1
			for segment in self.style_segments:
				while measure <= segment[0]:
					self.music[measure].__dict__.update(segment[1])


