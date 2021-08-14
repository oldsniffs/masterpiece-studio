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

new_duration rolls a new duration and passes it to distribute_duration to write it as notes to measure[f'{hand}_notes']
distribute_durations uses fill_distance to get the notes of specific durations which allows it to write tied notes
that do not cross beat divisions

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
		self.current_segment = self.segments[0]
		self.current_measure_index = 0
		self.current_measure = self.segments[0]['measures'][0]
		self.next_measure = self.segments[0]['measures'][1]
		self.increment = self.current_measure['style']['increment']
		self.hand = None
		self.count = 0 # count in measure
		self.remainder = 0
		self.tracker = 0
		self.terminus = 0
		self.note_tally = [0 for i in range(len(ALL_MASTERPIECE_NOTES))]

		self.fill_music()

	def fill_music(self):
		log_header(f"Filling Music")

		for segment in self.segments:
			self.current_segment = segment
			log_sub_header(f"Filling segment consisting of measures: {segment['start']} -- to -- {segment['stop']}")
			self.increment = segment['style']['increment']

			for measure in segment['measures']:
				self.current_measure = measure
				try:
					self.next_measure = segment['measures'][self.current_measure_index+1]
				except IndexError as e:
					log_info(f"End of segment {segment['index']} reached")
					self.next_measure = None
				self.current_style = self.current_measure['style']
				log_header(f"Filling Measure: {self.current_measure_index}")
				# Load overflow into live_durations
				for duration in self.current_measure['left_durations']:
					self.left_live_durations.append(duration)
				for duration in self.current_measure['right_durations']:
					self.right_live_durations.append(duration)

				for beat in range(self.current_measure['style']['timesig_num']):
					log_sub_header(f"== Measure {self.current_measure_index} -- Beat {beat} ==")
					for inc in range(int(1/self.increment)):  # number of increments per beat

						if self.current_measure['kites']:  # Place to process kites
							# load planned duration into live
							pass

						# Could use for self.hand = for hand in "left", "right"
						# If live durations were moved to segment, it could be accessed with string formatting.0

						# Right
						self.hand = "right"
						log_info(f"** switched to {self.hand} hand")

						# live_durations is empty, new duration required
						# New Prime
						if not self.right_live_durations:
							# Adjust weights -- [f'{self.hand}_prime_weights']
							weights = self.current_style['right_prime_weights']

							self.weigh_meter_strength(weights)

							self.new_duration()

						# Left
						self.hand = "left"
						log_info(f"** switched to {self.hand} hand")
						if not self.left_live_durations:
							self.new_duration()

						self.increment_count()

				self.current_measure_index += 1
				self.count = 0
				log_sub_header(f"End of measure {self.current_measure_index}")

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
		log_sub_header(f"New {self.hand} prime duration: {prime}")
		self.current_measure[f'{self.hand}_durations'].append((prime, self.count))
		self.__dict__[f'{self.hand}_live_durations'].append(prime)  # ref to duration, life

		self.distribute_duration(prime)

	# chops up duration into notes
	# put notes in right_music or left_music
	def distribute_duration(self, duration):
		log_info(f"Distributing duration {duration} at count {self.count} in the {self.hand} hand")
		self.remainder = duration
		notes = [] # (count, note)
		self.tracker = self.count
		division = int(self.count)
		self.terminus = self.count + duration

		if (overflow := self.terminus - self.current_style['timesig_num']) > 0:
			self.flow_over(overflow)
		final_division = int(self.terminus)

		if self.tracker != division:
			log_debug(f"Starting OFF-division, terminus at {self.terminus}")
		else:
			log_debug(f"starting ON-division, terminus at {self.terminus}")

		# if starting off-division start and reaches a division -- ascending order to endpoint
		if self.tracker != division and self.terminus >= division+1:
			# If distance to terminus can use a single note, do it

			if self.remainder in self.current_style['note_beat_values']:
				note = self.get_exact_note(self.remainder)
				self.write_note(note)
				self.tracker += self.remainder
				self.remainder -= note['beat_value']
				log_debug(f"remainder {self.remainder} better be 0")
				return

			# for bv in range(len(self.current_style['note_beat_values'])):
			# 	if self.remainder == self.current_style['note_beat_values'][bv]:
			# 		self.write_note(self.current_style['note_sheet'][bv])
			# 		self.tracker += bv
			# 		self.remainder -= bv  # better be 0
			# 		log_debug(f"remainder {self.remainder} better be 0")
			# 		return

			distance = division+1 - self.tracker
			fill_notes = self.fill_distance(distance, ascending=True)
			for fn in (fill_notes[:-1]):
				self.write_note(fn, engraving=["tie"])
				self.tracker += fn['beat_value']
				self.remainder -= fn['beat_value']
			if self.remainder:
				self.write_note(fill_notes[-1], engraving=["tie"])
			else:
				log_debug(f"Duration is ending, final note {fill_notes[-1]['name']} appending without tie")
				self.write_note(fill_notes[-1])
			self.remainder -= fill_notes[-1]['beat_value']
			self.tracker += fill_notes[-1]['beat_value']


		# Previous condition guarantees tracker is now on a division
		# Now get tracker to final division with whole beat notes
		if self.tracker < final_division and (distance := int(self.remainder)) > 1: # aren't these the same conditions?
			log_info(f"tracker is not in the final division -- remainder: {self.remainder}, tracker: {self.tracker}, terminus: {self.terminus}")

			# If one note can do it, end it here
			# Is this necessary? won't it be the first beat picked?
			if self.remainder in self.current_style['note_beat_values']:
				self.write_note(self.get_exact_note(self.remainder))
				self.tracker += distance
				self.remainder -= distance
				return

			notes = self.fill_distance(distance)
			self.tracker += distance

			for note in notes[:-1]:
				self.write_note(note, engraving=["tie"])
			if self.tracker < self.terminus:
				self.write_note(notes[-1])
			else:
				self.write_note(notes[-1], engraving=["tie"])
			self.remainder -= distance

		# final_division reached with a remainder
		if self.remainder:
			notes = self.fill_distance(self.remainder)
			for note in notes[:-1]:
				self.write_note(note, engraving=["tie"])
			self.write_note(notes[-1])

	def distribute_duration_while_loop(self, duration):  # Alternative implementation structure
		# Be sure the variables are ready for loop
		while self.remainder:
			ascending = False
			# find distance
			# mid -> div make ascending
			# biggest single once on div
			# tie until last note
			# make assignment - note or set of notes

	# Move any overflow duration to next measure and adjust self.terminus and self.remainder accordingly
	def flow_over(self, overflow):
		log_info(f"terminus {self.terminus} is outside current measure. Sending overflow {overflow} to next measure in segment")
		self.terminus -= overflow
		self.remainder -= overflow
		try:
			self.next_measure[f'{self.hand}_durations'].append(overflow)
			log_debug(
				f"overflow {overflow} has been appended to next measure @ index: {self.current_measure_index + 1}")
		except TypeError:  # self.next_measure is None because current measure ends segment
			log_debug(f"Overflow cancelled because segment ended")

	def write_note(self, note, engraving=[]):
		note['engraving'] = engraving  # Engraving is a list of keyword strings
		note['start'] = self.tracker
		self.current_measure[f"{self.hand}_music"].append(note)
		log_info(f"{self.hand.capitalize()} Note {note['name']} written -- start: {note['start']}  beat_value:{note['beat_value']}")
		# record to note_tally
		self.note_tally[note['masterpiece_index']] += 1


	# Returns untied list of notes in descending order that fills an amount of beats
	def fill_distance(self, distance, ascending=False):
		log_debug(f"Filling_distance({distance}, ascending={ascending})")
		notes = []
		while distance:
			note = self.get_largest_note(distance)
			notes.append(note)
			log_debug(f"loading {note['name']} ({note['beat_value']}) note to fill distance {distance}")
			distance -= note['beat_value']

		if ascending:
			notes = notes[::-1]
		return notes

	def get_largest_note(self, distance):
		log_debug(f"Getting largest note for distance {distance}")
		for note in self.current_style['note_sheet_descending']:
			if note['beat_value'] <= distance:
				f"got {note['name']} note, beat value: {note['beat_value']}"
				return note

	def get_exact_note(self, distance):
		log_debug(f"getting exact note for distance {distance}")
		for note in self.current_style['note_sheet_descending']:
			if note['beat_value'] == distance:
				f"success! {note['name']} note, beat value: {note['beat_value']}, matches desired beat value of {distance}"
				return note
			else:
				f"failure! this shouldn't happen"

	# increments count and live durations, removes dead ones
	def increment_count(self):
		log_debug(f"Incrementing count: {self.count} by {self.increment}")
		self.count += self.increment
		self.tracker = 0
		self.hand = "right" # for debug
		for live_durations in self.right_live_durations, self.left_live_durations:
			chopping_block = []
			for ld in range(len(live_durations)):
				live_durations[ld] -= self.increment
				if live_durations[ld] == 0:
					chopping_block.append(ld)

			if chopping_block:
				for chop in reversed(chopping_block):
					log_debug(f"Chopping index {chop} from {self.hand}_live_durations: {live_durations}")
					del live_durations[chop]
			self.hand = "left" # for debug

		if self.count % .25 == 0:
			log_info(f"Increment brings count to {self.count}")


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


