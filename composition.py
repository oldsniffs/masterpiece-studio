"""

Measure dictionaries
number: integer
flags: list of strings
right: list of notes
left: list of notes

"""

from custom_logging import *
from notes import *

# Composition class
#
# ===================================
#
# Generates music from user input:
# 1) form_segments converts user input from argument raw_segments into use-ready form as segments attribute
# 2) fill_music generates music, stored in segment's []

# Composition.segments[...]['music'] holds underlying musical information studio can convert to output formats

# Possible return formats for technical-side use

# use-ready segments have a "kites" list
# this is a system of injecting special musical events "randomly"
# kites can indicate special events for the measure
# music gen, although done by measure, will also track beat in segment and look for kites to turn on.

# self.segments list holds segment dicts

# ['kite pool'] is fifo queue that waits for next event's measure/beat number to come up to either
# 1) event that acts now
# 2) toggle a bool
# kite: ((measure, beat), kite)

# Composition.segment: {'boundaries':(start measure, end measure, total measures),'musical_parameters':{dict of parameters}, measures:[list of measures]]}
# segment dicts hold data for generating segment's music
# a segment's music item holds a list of measure dictionaries

# measure: {'number':integer, 'musical_parameters':points to segment's item, 'music':}
# measure dicts hold reference to parameters

# "note" in a measure needs: note, scientific pitch notation, engraving info

# form_segments will
# fill_music will

class Composition:
	def __init__(self, song_info, segments):

		log_header('Composition constructor starting')

		# song-level info
		self.song_info = song_info

		# [(range of measures, musical parameters as dictionary),...]
		self.segments = segments

		# generate music by operating on self.music
		self.fill_music()

	def place_kites(self, raw_segment):
		# takes a raw_segment reference and returns a kite pool list
		return [
			((1, 0), raw_segment['pairingOn']),
		]

	def send_kite(self, target, kite):
		pass

	# place flags for pairings, syncs, other special occurences
	def allocate_flags(self):
		pass

	def fill_music(self):
		for segment in self.segments:
			pass

	def fill_right(self, measure):
		pass

	def fill_left(self, measure):
		pass

	def get_musical_parameters(self, measure_number):
		pass

	# Utility ========================

	def music_total_measures(self):
		total_measures = 0
		for segment in self.music:
			total_measures += len(segment)


