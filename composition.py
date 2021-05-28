import random

from custom_logging import *
from notes import *

# Composition class
#
# ===================================
#
# Generates music from user input:

# Composition.segments[...]['music'] holds underlying musical information studio can convert to output formats

# use-ready segments have a "kites" list
# this is a system of injecting special musical events "randomly"
# kites can indicate special events for the measure
# music gen, although done by measure, will also track beat in segment and look for kites to turn on.

# self.segments list holds segment dicts

# ['kite pool'] is fifo queue that waits for next event's measure/beat number to come up to either (music gen should check if top item is "ready")
# 1) initiate an event immediately
# 2) toggle a bool  -- can turn on checking for next good time to insert event
# kite: ((measure, beat), kite)

# segment dicts are: {'range':(start measure, end measure, total measures),'style':{dict of parameters}, measures:[list of measures]]}
# each segment is given ['measures'] - a list of measure dictionaries to be filled

# measure dicts are: {'number':integer, 'musical_parameters':points to segment's item, 'kites':[], 'durations':[], 'right_music':[], 'left_music':[]}
# 'right_durations' and 'left_durations' contain sequential lists of prime durations rolled in that measure
# 'right_music' and 'left_music' contain sequential list of notes, which precisely represent the sheet music

# notes are: {	type: "note type",
# 						duration ,
# 						starting beat in measure,
# 						scientific pitch notation,
# 						extra engraving info,
# 						}

# fill_music generates music, filling in each measure's ['music'] list
# self.full_music() returns full music lists for right and left hands

# If a duration the hand's durations are depleted, a new_prime_duration is called, and the returned duration is recorded
# in ['right_durations'] or ['left_durations']
# Then, whatever durations have a balance are processed
#
# 5/26
# The above seems wrong. More simply, the duration can be stored in ['durations'], a list, and referenced from there by
# the generator as it applies it's balance to the music, in whatever way appropriate, as notes in left or right music,
# modifying the duration's ['balance'] integer as it does


class Composition:
	def __init__(self, configuration):

		log_header('Composition constructor starting')

		self.name = configuration.composition_name

		self.segments = configuration.segments

		self.fill_music()
		self.music = self.full_music()  # lists for right and left notation compiled from the segments

	def fill_music(self):
		log_header(f"Filling Music")

		right_tract = []
		left_tract = []

		for segment in self.segments:
			log_sub_header(f"Filling segment between measures: {segment['range'][0]} -- and -- {segment['range'][1]}")

			for measure in segment['measures']:
				log_info(f"Filling Measure: {measure['number']}")
				increment = measure['style']['increment']

				for beat in range(measure['style']['timesig_num']):
					log_debug(f"== Beat {beat} ==")
					for inc in range(int(1/increment)):  # number of increments per beat

						if measure['kites']:  # Place to process kites
							pass

						# Process tract
						# Right
						if not right_tract:
							prime = self.new_prime(measure['prime_weights'])# Here, weights could be modified for "snap-fitting" preferences
							right_tract.append(prime)
							measure['right_durations'].append(prime)

						# Left
						if not left_tract:
							# Skew weights for left if "dragged"
							prime = self.new_prime(measure['prime_weights'])
							right_tract.append(prime)
							measure['right_durations'].append(prime)

						# increment right_live_durations
						self.increment_live_durations(right_tract, increment)
						self.increment_live_durations(left_tract, increment)

						# measure.music.append({'note_type': note_type, 'duration': duration, 'start_beat': start_beat, 'spn': spn, 'engraving_info': engraving_info})

	def new_duration(self, weights):
		random.choices(weights)

	def new_limited(self):  #  like new prime with limited min and/or max range
		pass

	def increment_live_durations(self, live_durations, increment):
		for live_duration in live_durations:
			live_duration['life'] -= increment
			if not live_duration['life']:
				live_durations.remove(live_duration)

	# deliver a kite to a segment measure
	def send_kite(self, target, kite):
		pass

	# place flags for pairings, syncs, other special occurences
	def allocate_flags(self):
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

	def full_music(self):
		log_debug(f"full_music")
		for segment in self.segments:
			pass

	# Data Retrieval ========================

	def music_total_measures(self):
		total_measures = 0
		for segment in self.music:
			total_measures += len(segment)


