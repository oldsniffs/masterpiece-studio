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

notes are: {type: "note type", 
			duration: duration,
			starting beat in measure: <- self.count, *
			scientific pitch notation: "" <-,
			extra engraving info: [] <-}
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
		self.count = 0 # count in measure
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

			for m in len(range(segment['measures'])):
				self.current_measure = segment['measures'][m]
				self.next_measure = segment['measure'][m+1]
				self.current_style = self.current_measure['style']
				log_info(f"Filling Measure: {m+1}")
				# Load overflow into live_durations
				for duration in self.current_measure['left_durations']:
					self.left_live_durations.append(duration)
				for duration in self.current_measure['right_durations']:
					self.right_live_durations.append(duration)

				for beat in range(self.current_measure['style']['timesig_num']):
					log_debug(f"== Beat {beat} ==")
					for inc in range(int(1/self.increment)):  # number of increments per beat

						if self.current_measure['kites']:  # Place to process kites
							# load planned duration into live
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
							weights = self.current_style['right_prime_weights']

							self._weight_meter_strength(weights)
							# meter_strength adjustment (replaces old "snapping")

							prime = self.new_duration()

							# properly distribute duration
							self.distribute_duration(prime)

						for live_duration in self.right_live_durations:
							# Establish hierarchy of any beat marks crossed
							pass

						# Left
						self.hand = "left"
						if not self.left_live_durations:
							# Skew weights for left if "dragged"   ---- 8/4 move to finalize song params
							prime_duration = self.new_duration()
							self.current_measure['left_durations'].append(prime_duration)
							self.left_live_durations.append(prime_duration)

						self.increment_count()

				self.count = 0

						# measure.music.append({'note_type': note_type, 'duration': duration, 'start_beat': start_beat, 'spn': spn, 'engraving_info': engraving_info})

	def _weigh_meter_strength(self, weights):
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
		self.__dict__[f'{self.hand}_live_durations'].append([prime, prime])  # ref to duration, life

		self.distribute_duration(prime)

	# chops up duration into notes
	# put notes in right_music or left_music
	def distribute_duration(self, duration):
		log_info(f"Distributing duration {duration} at from count {self.count}")
		# break on division_beats
		# iterate through succeeding division beats in durations life
		remainder = duration
		notes = [] # (count, note)
		tracker = self.count
		division = int(self.count)
		terminus = self.count + duration
		if terminus > self.current_style['timesig_num']:
			terminus = self.current_style['timesig_num']
		final_division = int(terminus)

		# if start is off division start and reaches a division -- ascending order to endpoint
		if self.count != division and terminus >= division+1:
			distance = division+1 - self.count
			fill_notes = self.fill_gap(distance)
			for fn in reversed(fill_notes):
				self.current_measure[f"{self.hand}_music"].append(fn)
			tracker += distance
			remainder -= distance

		# Previous if statement guarantees that if still distributing, tracker is now on a division
		while distance:= terminus - tracker > 0:
			# measure


			# process to end of measure, send remainder to next measure
			print(distance)
			# does it end before next division?
			if remainder < 1:
				distance = remainder
			# how many more divisions it crosses?
			remaining_divs = int(remainder)
			# does it cross a measure?
			if tracker + remaining_divs > self.current_style['timesig_num']:
				pass

			# cut

			for note in self.fill_gap(distance):
				self.current_measure[f"{self.hand}_music"].append(n)
			return

		# end of measure reached with remainder
		if remainder:
			self.next_measure[f"{self.hand}_durations"].append(remainder)


		# get remaining division markers
		# iterate remaining division markers
		for b in range(division, self.current_style['timesig_num']):
			if self.count != b: # Start OFF division
				log_info(f"at count {self.count}, we are starting OFF a division")

				while tracker < b:
					pass

			# if strong, go as far as possible
			else: # Start ON division
				log_info(f"at count {self.count}, we are starting ON a division")

			# denominate with meter unit

			# send flow_over to next measure (
		pass

	def _assign_notes(self, notes):
		pass

	# Returns untied list of notes in ascending order that fills an amount of beats
	# needs to get notes by checking their beat values
	def fill_gap(self, gap):
		notes = []
		while gap:
			for note in self.current_style['note_sheet']:
				if note['beat_value'] <= gap:
					notes.append(note)
					gap -= note['beat_value']
		return notes


	# increments durations, removes dead ones
	def increment_count(self):
		self.count += self.increment
		for live_duration in + self.left_live_durations + self.right_live_durations:
			live_duration[1] -= self.increment
			if not live_duration[1]:
				del[live_duration]

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


