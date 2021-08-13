import random

from src.custom_logging import *
from notes import *

"""
Composer class

===================================

Generates music from user input:

Composer class generates a random piece of music from a user determined configuration
The music attribute is the main item of interest. It holds lists representing complete notational information for each hand

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

notes are: {'name':, real world note name,
			'masterpiece_index': index int,
			'beat_value': duration of beat value,
			'start': <- insertion point tracker, *
			'spn': "" <- scientific pitch notation,
			'engraving': [] <- extra engraving info}
* "<-" means it gets added in by the Composer class

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
		self.next_measure = self.segments[0]['measures'][1]
		self.increment = self.current_measure['style']['increment']
		self.hand = None
		self.count = 0 # count in measure
		self.remainder = 0
		self.tracker = 0
		self.terminus = 0
		self.note_tally = [0 for i in range(len(ALL_NOTES))]

		self.fill_music()

	def fill_music(self):
		log_header(f"Filling Music")

		for segment in self.segments:
			self.current_segment = segment
			log_sub_header(f"Filling segment consisting of measures: {segment['start']} -- and -- {segment['stop']}")
			self.increment = segment['style']['increment']

			for m in range(len(segment['measures'])):
				self.current_measure = segment['measures'][m]
				try:
					self.next_measure = segment['measures'][m+1]
				except IndexError as e:
					self.next_measure = None
				self.current_style = self.current_measure['style']
				log_info(f"Filling Measure: {m+1}")
				# Load overflow into live_durations
				for duration in self.current_measure['left_durations']:
					self.left_live_durations.append(duration)
				for duration in self.current_measure['right_durations']:
					self.right_live_durations.append(duration)

				for beat in range(self.current_measure['style']['timesig_num']):
					log_info(f"== Beat {beat} ==")
					for inc in range(int(1/self.increment)):  # number of increments per beat

						if self.current_measure['kites']:  # Place to process kites
							# load planned duration into live
							pass

						# Right
						self.hand = "right"
						# live_durations is empty, new duration required

						# New Prime
						if not self.right_live_durations:
							# Adjust weights -- [f'{self.hand}_prime_weights']
							weights = self.current_style['right_prime_weights']

							self.weigh_meter_strength(weights)

							self.new_duration()

						for live_duration in self.right_live_durations:
							# Establish hierarchy of any beat marks crossed
							pass

						# Left
						self.hand = "left"
						if not self.left_live_durations:
							self.new_duration()

						self.increment_count()

				self.count = 0

						# measure.music.append({'note_type': note_type, 'duration': duration, 'start_beat': start_beat, 'spn': spn, 'engraving_info': engraving_info})

	def weigh_meter_strength(self, weights):
		if random.randint(1,100) < self.current_style['meter_strength']:

			# get snapping durations - list of snapping values
			# cycle all duration weights, shift their weight to nearest snapping value

			# change indices of unwanted durations to 0

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
		self.__dict__[f'{self.hand}_live_durations'].append(prime)  # ref to duration, life

		self.distribute_duration(prime)

	# chops up duration into notes
	# put notes in right_music or left_music
	def distribute_duration(self, duration):
		log_info(f"Distributing duration {duration} at from count {self.count} in the {self.hand} hand")
		# break on division_beats
		self.remainder = duration
		notes = [] # (count, note)
		self.tracker = self.count
		division = int(self.count)
		self.terminus = self.count + duration

		# Move any overflow duration to next measure and adjust this duration's terminus accordingly
		if (overflow := self.terminus - self.current_style['timesig_num']) > 0:
			log_info(f"self.terminus {self.terminus} is outside current measure. Sending overflow to next measure in segment")
			self.terminus = self.current_style['timesig_num']
			try:
				self.next_measure[f'{self.hand}_durations'].append(overflow)
				self.remainder -= overflow
			except TypeError:  # self.next_measure is None because current measure ends segment
				log_debug(f"Overflow cancelled because segment ended")
		final_division = int(self.terminus)

		# if start is off division start and reaches a division -- ascending order to endpoint
		if self.tracker != division and self.terminus >= division+1:
			log_debug(f"starting OFF, terminus at {self.terminus}")
			distance = division+1 - self.tracker
			fill_notes = reversed(self.fill_distance(distance))
			for fn in fill_notes[1:]: #apply tied
				self.current_measure[f"{self.hand}_music"].write_note(fn, engraving="tie")
				self.tracker += fn['beat_value']
			if self.remainder:
				self.current_measure[f'{self.hand}_music'].write_note(fill_notes[1], engraving="tie")
			else:
				self.current_measure[f'{self.hand}_music'].write_note(fill_notes[1])
			self.tracker += distance
			self.remainder -= distance

		# Previous condition guarantees that if still distributing, self.tracker is now on a division
		# Now measure and cut the distance into notes until self.remainder is 0
		# If adjustments to distribution need to be made it should be in the measuring process
		while self.remainder > 0:
			log_info(f"measuring note for remainder: {self.remainder}, tracker: {self.tracker}, terminus: {self.terminus}")
			# Measure (verb)
			# does it end before next division?
			if self.remainder < 1:
				for note in self.fill_distance(self.remainder):
					pass
			# measure number of whole divisions
			else:
				distance = int(self.remainder)
			notes = self.fill_distance(distance)

			# Cut

			for note in self.fill_distance(distance):
				self.current_measure[f"{self.hand}_music"].append(note)
			return

		# end of measure reached with self.remainder
		if self.remainder:
			try:
				self.next_measure[f"{self.hand}_durations"].append(self.remainder)
			except TypeError as e:
				log_info(f"Type Error hit processing overflow, indicating end of measure")

	def write_note(self, note, engraving=""):
		note['engraving'] = engraving  # Engraving is string of comma separated keywords
		self.current_measure[f"{self.hand}_music"].append(note)

	# Returns untied list of notes in ascending order that fills an amount of beats
	# needs to get notes by checking their beat values
	def fill_distance(self, distance):
		notes = []
		while distance:
			for note in self.current_style['note_sheet']:
				if note['beat_value'] <= distance:
					notes.append(note)
					distance -= note['beat_value']
		return notes


	# increments count and live durations, removes dead ones
	def increment_count(self):
		log_info(f"Incrementing count: {self.count} by {self.increment}")
		self.count += self.increment
		log_debug(f"left live durations: {self.left_live_durations}\nright live durations: {self.right_live_durations}")
		all_live = self.right_live_durations + self.left_live_durations
		for live_durations in self.right_live_durations, self.left_live_durations:
			chopping_block = []
			for ld in range(len(live_durations)):

				print(live_durations[ld])
				live_durations[ld] -= self.increment
				print(live_durations[ld])
				if live_durations[ld] == 0:
					chopping_block.append(ld)

			for chop in reversed(chopping_block):
				log_debug(f"Chopping index {chop} from live durations: {live_durations}")
				del live_durations[chop]



	# Generation Utility ========================

	# Probably Dep
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


