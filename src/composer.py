import random

from src.custom_logging import *
from notes import *

"""
Composer class

===================================

Generates music from user input:

Composer.segments[...]['music'] holds underlying musical information studio can convert to output formats

use-ready segments have a "kites" list
this is a system of injecting special musical events "randomly"
kites can indicate special events for the measure
music gen, although done by measure, will also track beat in segment and look for kites to turn on.

self.segments list holds segment dicts

['kite pool'] is fifo queue that waits for next event's measure/beat number to come up to either (music gen should check if top item is "ready")
1) initiate an event immediately
2) toggle a bool  -- can turn on checking for next good time to insert event
kite: ((measure, beat), kite)

segment dicts are: {'start':int, 'stop': int, 'length': int, 'style':{dict of parameters}, measures:[list of measures]]}
each segment contains ['measures'] - a list of measure dictionaries to be filled

live_durations [duration, balance] - 8/4 just balance?
 'durations', 'music' 

measure dicts are: {'number':integer, 'musical_parameters':points to segment's item, 'kites':[], 'right_durations':[],'left_durations':[], 'right_music':[], 'left_music':[]}
'right_durations' and 'left_durations' contain sequential lists of prime durations beginning in that measure
'right_music' and 'left_music' contain sequential list of notes, which precisely represent the sheet music

durations are drawn from ['style']['duration_sheet'] -- (duration, count)
notes are drawn from ['style']['note_sheet']

durations are: (value, weight)

notes are: {type: "note type", 
			duration: beats,
			starting beat in measure: beat,
			scientific pitch notation: "",
			extra engraving info: []}

fill_music generates music, filling in each measure's ['music'] list
self.full_music() returns full music lists for right and left hands
"""

class Composer:
	def __init__(self, configuration):

		log_header('Composition constructor starting')

		self.name = configuration.composition_name

		self.segments = configuration.segments

		# Initialize Dynamic Generation Variables
		self.right_live_durations = []
		self.left_live_durations = []
		self.current_measure = self.segments[0]['measures'][0]
		self.increment = self.current_measure['style']['increment']
		self.count = 0
		self.hand = None
		self.note_tally = [0 for i in range(len(ALL_NOTES))]

		self.fill_music()
		self.music = self.full_music()  # lists for right and left notation compiled from the segments - 7/9 Likely dep

	def fill_music(self):
		log_header(f"Filling Music")

		for segment in self.segments:
			self.current_segment = segment
			log_sub_header(f"Filling segment consisting of measures: {segment['start']} -- and -- {segment['stop']}")
			self.increment = segment['style']['increment']

			for measure in segment['measures']:
				self.current_measure = measure
				log_info(f"Filling Measure: {measure['number']}")

				for beat in range(measure['style']['timesig_num']):
					log_debug(f"== Beat {beat} ==")
					for inc in range(int(1/self.increment)):  # number of increments per beat

						if measure['kites']:  # Place to process kites
							pass

						"""Must fulfill:
						1. Proper duration division
						What: durations do not cross through beats if they did not start on one
						How: If duration does not start on a beat and crosses a beat marker, spawn a note or notes
						tied together to the start of the next beat, then spawn tied notes to complete the duration's 
						term
						Precisely how durations should be allocated among it's tied notes before and after beats:
						
						2. Sync factor
						3. Left weight modification -
						
						8/1 As of, note proportion maintenance is in design, but not being implemented yet 
						"""

						# Right
						self.hand = "right"
						# live_durations is empty, new duration required

						# New Prime
						if not self.right_live_durations:
							# Adjust weights -- [f'{self.hand}_prime_weights']
							# "snapping" -- Use snap slider + distance to beat markers + note proportion needs


							prime = self.new_duration()

						for live_duration in self.right_live_durations:
							# Establish hierarchy of any beat marks crossed
							pass

						# Left
						self.hand = "left"
						if not self.left_live_durations:
							# Skew weights for left if "dragged"   ---- 8/4 move to finalize song params
							prime_duration = self.new_duration()
							measure['left_durations'].append(prime_duration)
							self.left_live_durations.append(prime_duration)

						self.increment_count()

				self.count = 0

						# measure.music.append({'note_type': note_type, 'duration': duration, 'start_beat': start_beat, 'spn': spn, 'engraving_info': engraving_info})

	# chops up duration into notes
	# put notes in right_music and left_music
	def distribute_duration(self, duration):
		pass

	def snap(self, weights):
		pass

	# Adjust weights to maintain proportion
	def proportion_adjust(self, weights):
		return

	# Return duration index
	def new_duration(self):
		prime = self.current_measure['style']['duration_sheet'][random.choices(PRIME_DURATIONS_INDEX, self.current_measure['style'][f'{self.hand}_prime_weights'])[0]] # a random duration from the duration_sheet
		log_debug(f"new prime duration: {prime}")
		self.current_measure[f'{self.hand}_durations'].append((prime, self.count))
		self.__dict__[f'{self.hand}_live_durations'].append([prime, prime])  # ref to duration, life

		self.distribute_duration(prime)

	# increments durations, removes dead ones
	def increment_count(self):
		self.count += self.increment
		for live_duration in + self.left_live_durations + self.right_live_durations:
			live_duration[1] -= self.increment
			if not live_duration[1]:
				del[live_duration]

	# Generation Utility ========================

	def check_beat_strength(self, duration, count):
		log_debug(f"Checking if a duration {duration} on count {count} is strong")
		if (count/duration[1]) % 2 == 0:
			log_debug(f"STRONG")
			return True
		else:
			log_debug(f"WEAK")
			return False

	# Info ========================
	def music_total_measures(self):
		total_measures = 0
		for segment in self.music:
			total_measures += len(segment)


