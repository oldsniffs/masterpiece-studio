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
# 1) form_structure converts user input from argument raw_segments into use-ready form as segments attribute
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
# 2) toggle a bool  -- can turn on checking for next good time to insert event
# kite: ((measure, beat), kite)
# TODO: Segment or measure level?

# configuration.segment: {'range':(start measure, end measure, total measures),'style':{dict of parameters}, measures:[list of measures]]}
# each segment is given ['measures'] - a list of dictionaries to be filled

# these measures are: {'number':integer, 'musical_parameters':points to segment's item, 'kites':[], 'right_music':}
# measure['right_music'] and ['left_music'] contains sequential list of notes

# these notes are: {	type: "note type",
# 						duration ,
# 						starting beat in measure,
# 						scientific pitch notation,
# 						extra engraving info,
# 						}

# fill_music generates music, filling in each measure's ['music'] list
# self.full_music() returns combined music lists for right and left hands


class Composition:
	def __init__(self, configuration):

		log_header('Composition constructor starting')

		self.configuration = configuration

		# With segment boundaries and timesigs confirmed, load duration_sheet to the style and add the "empty" measures
		# list
		for segment in self.configuration:
			segment['style'].update(duration_sheet(segment['style']['timesig_den']))
			segment['measures'] = [{
				'number': measure,
				'style': segment['style'],
				'kites':[],
				'right_music':[],
				'left_music':[]
			} for measure in range(segment['range'][0], segment['range'][1]+1)]

		self.fill_music()
		self.music = self.full_music()  # lists for right and left notation

	def fill_music(self):
		log_header(f"Filling Music")

		for segment in self.configuration.segments:
			log_sub_header(f"Filling segment between measures: {segment['range'][0]} -- and -- {segment['range'][1]}")

			for measure in segment['measures']:
				self.fill_measure(measure, segment)

	def fill_measure(self, measure, segment):
		log_info(f"Filling Measure: {measure['number']}")
		beat = 1

		while beat <= measure['style']['timesig_num']:
			f" == Beat {beat} =="

			# Right

			# Left

			measure.music.append({'note_type': note_type, 'duration': duration, 'start_beat': start_beat, 'spn': spn, 'engraving_info': engraving_info})


	# deliver a kite to a segment measure
	def send_kite(self, target, kite):
		pass

	# place flags for pairings, syncs, other special occurences
	def allocate_flags(self):
		pass

	def fill_right(self, measure):
		pass

	def fill_left(self, measure):
		pass

	# Generation Utility
	def check_beat_strength(self, duration, count):
		log_debug(f"Checking if a duration {duration} on count {count} is strong")
		if (count/duration[1]) % 2 == 0:
			log_debug(f"STRONG")
			return True
		# Might not need this else
		else:
			log_debug(f"WEAK")
			return False

	# Data Retrieval ========================

	def music_total_measures(self):
		total_measures = 0
		for segment in self.music:
			total_measures += len(segment)


