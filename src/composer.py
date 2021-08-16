import random
import os

from custom_logging import *
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

measure dicts are: {'number':integer, 
					'musical_parameters':points to segment's item, 
					'kites':[], 
					'right_durations':[],
					'left_durations':[], 
					'right_music':[], 
					'left_music':[]}
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
		self.filename = configuration.composition_filename
		self.filepath = configuration.composition_filepath

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
		self.fill_rhythm()
		self.fill_pitches()

		log_header(f"Note Check")
		for segment in self.segments:
			for measure in segment['measures']:
				log_debug(f"right_music")
				for note in measure['right_music']:
					print(note)
				log_debug(f"left_music")
				for note in measure['left_music']:
					print(note)

	# fill_rhythms and Supporting Methods ===========

	def fill_rhythm(self):
		log_header(f"Filling Music")

		for segment in self.segments:
			self.current_segment = segment
			log_sub_header(f"Filling segment consisting of measures: {segment['start']} -- to -- {segment['stop']}")
			self.increment = segment['style']['increment']

			for measure in segment['measures']:
				self.current_measure = measure
				self.current_style = self.current_measure['style']
				try:
					self.next_measure = segment['measures'][self.current_measure_index+1]
				except IndexError as e:
					log_info(f"End of segment {segment['index']} reached")
					self.next_measure = None
				log_header(f"Filling Measure: {measure['number']}")
				# Load overflow into live_durations
				if measure['kites']['overflow']:
					log_debug(f"Overflow kite ")
					self.hand = "right"
					for duration in self.current_measure['right_durations']:
						log_debug(f"found overflow in right_durations: {duration}")
						self.distribute_duration(duration)
						self.right_live_durations.append(duration)
					self.hand = "left"
					for duration in self.current_measure['left_durations']:
						log_info(f"found overflow in left_durations: {duration}")
						self.distribute_duration(duration)
						self.left_live_durations.append(duration)

				for beat in range(self.current_measure['style']['timesig_num']):
					log_sub_header(f"== Measure {measure['number']} -- Beat {beat} ==")
					for inc in range(int(1/self.increment)):  # number of increments per beat

						if self.current_measure['kites']:  # Place to process kites
							# load planned duration into live
							pass

						# For tighter code:
						# Could use for self.hand = for hand in "left", "right"
						# If live durations were moved to segment or above, it could be accessed with string formatting

						# Right
						self.hand = "right"

						# live_durations is empty, new duration required
						# New Prime
						if not self.right_live_durations:
							# Adjust weights -- [f'{self.hand}_prime_weights']
							weights = self.current_style['right_prime_weights']

							self.weigh_meter_strength(weights)

							self.new_duration()

						# Left
						self.hand = "left"
						if not self.left_live_durations:
							self.new_duration()

						self.increment_count()

				self.current_measure_index += 1
				self.count = 0

				# With harmony implemented, this debug would need to track only a "top line" of notes somehow
				right_beat_values = 0
				left_beat_values = 0
				for note in measure['right_music']:
					right_beat_values += note['beat_value']
				for note in measure['left_music']:
					left_beat_values += note['beat_value']
				log_debug(f"Measure ending with {right_beat_values} beat value of notes in right and {left_beat_values} in left")

				log_sub_header(f"End of measure {self.current_measure_index}")

	def weigh_meter_strength(self, weights):
		if random.randint(1, 100) < self.current_style['meter_strength']:

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
		duration_notes = []
		self.remainder = duration
		self.tracker = self.count
		division = int(self.count)
		self.terminus = self.count + duration
		# Overflow
		overflowed = False
		if (overflow := self.terminus - self.current_style['timesig_num']) > 0:
			overflowed = True
			self.flow_over(overflow)
		final_division = int(self.terminus)

		if self.tracker != division:
			log_debug(f"Starting OFF-division {self.tracker}, terminus at {self.terminus}")
		else:
			log_debug(f"Starting ON-division {division}, terminus at {self.terminus}")

		# if starting off-division start and reaches a division -- get to final division ascending order to endpoint
		if self.tracker != division and self.terminus >= division+1:
			log_debug(f"Tracker {self.tracker} != division {division} and terminus {self.terminus} >= next division {division+1}")

			# If terminus ends on a division and distance to terminus can use a single note, do it
			if self.terminus == int(self.terminus) and not overflowed:
				log_debug(f"Terminus {self.terminus} is on a division. Trying to match an exact note for remainder {self.remainder}")
				for beat_value in self.current_style['note_beat_values']:
					if beat_value == self.remainder:
						note = self.get_exact_note(beat_value)
						log_debug(f"Found note {note['name']} with beat value {note['beat_value']} = {beat_value}")
						duration_notes.append(note)
						self.tracker += note['beat_value']
						self.remainder -= note['beat_value']
			else:
				distance = division+1 - self.tracker
				log_debug(f"distance to next division: {distance}")
				fill_notes = self.fill_distance(distance, ascending=True)
				for fn in (fill_notes):
					duration_notes.append(fn)
					self.tracker += fn['beat_value']
					self.remainder -= fn['beat_value']

		# Previous condition guarantees tracker is now on a division
		# Now get tracker to final division with whole beat notes
		if self.tracker < final_division and (distance := int(self.remainder)) >= 1: # aren't these the same conditions?
			log_info(f"tracker is not in the final division -- remainder: {self.remainder}, tracker: {self.tracker}, terminus: {self.terminus}")

			# If one note can do it, end it here
			# Is this necessary? won't it be the first beat picked?
			if self.remainder in self.current_style['note_beat_values']:
				duration_notes.append(self.get_exact_note(self.remainder))
				self.tracker += self.remainder
				self.remainder -= self.remainder

			else:
				notes = self.fill_distance(distance)
				for note in notes:
					duration_notes.append(note)
					self.tracker += note['beat_value']
					self.remainder -= note['beat_value']

		# final_division reached with a remainder
		if self.remainder:
			log_debug(f"In duration's final division: {final_division}, at tracker {self.tracker} with remainder: {self.remainder}")
			notes = self.fill_distance(self.remainder)
			for note in notes:
				duration_notes.append(note)

		for d in range(len(duration_notes)):
			if d == len(duration_notes)-1 and self:
				self.write_note(duration_notes[d])
			else:
				self.write_note(duration_notes[d], engraving=["tie"])


	def distribute_duration_while_loop(self, duration):  # Alternative implementation
		# Prepare variables for loop
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
		if self.next_measure:
			self.next_measure[f'{self.hand}_durations'].append(overflow)
			self.next_measure['kites']['overflow'] = True
			log_debug(f"overflow {overflow} has been appended to measure {self.next_measure['number']}\nIt's durations are Right: {self.next_measure['right_durations']}\nLeft: {self.next_measure['left_durations']}")

	def write_note(self, note, engraving=[]):
		note['engraving'] = engraving  # Engraving is a list of keyword strings
		note['start'] = self.tracker
		self.current_measure[f"{self.hand}_music"].append(note)
		log_info(f"{self.hand.capitalize()} Note {note['name']} written -- start: {note['start']}  beat_value:{note['beat_value']} engraving: {engraving}")
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
				return note.copy()

	def get_exact_note(self, distance):
		log_debug(f"getting exact note for distance {distance}")
		for note in self.current_style['note_sheet_descending']:
			if note['beat_value'] == distance:
				f"success! {note['name']} note, beat value: {note['beat_value']}, matches desired beat value of {distance}"
				return note.copy()
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

	# fill_pitches and Supporting Methods ============

	def fill_pitches(self): # hard coded while dev
		for segment in self.segments:
			for measure in segment['measures']:
				for note in measure['left_music']:
					log_debug(f"Adding pitch to {note}")
					note['spn'] = "A3"
				for note in measure['right_music']:
					note['spn'] = "E4"

	# Generation Utility =============================

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


