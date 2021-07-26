import random

from src.custom_logging import *
from notes import *

# Composer class
#
# ===================================
#
# Generates music from user input:

# Composer.segments[...]['music'] holds underlying musical information studio can convert to output formats

# use-ready segments have a "kites" list
# this is a system of injecting special musical events "randomly"
# kites can indicate special events for the measure
# music gen, although done by measure, will also track beat in segment and look for kites to turn on.

# self.segments list holds segment dicts

# ['kite pool'] is fifo queue that waits for next event's measure/beat number to come up to either (music gen should check if top item is "ready")
# 1) initiate an event immediately
# 2) toggle a bool  -- can turn on checking for next good time to insert event
# kite: ((measure, beat), kite)

# segment dicts are: {'start':int, 'stop': int, 'length': int, 'style':{dict of parameters}, measures:[list of measures]]}
# each segment contains ['measures'] - a list of measure dictionaries to be filled

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
# the generator as it applies its balance to the music, in whatever way appropriate, as notes in left or right music,
# modifying the duration's ['balance'] integer as it does.
# 7/9 If Composer / Composition pattern is used, Composer only needs to track "durations" in one place


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

		self.fill_music()
		self.music = self.full_music()  # lists for right and left notation compiled from the segments - 7/9 Likely dep

	def fill_music(self):
		log_header(f"Filling Music")

		for segment in self.segments:
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

						# Right
						# tract is empty, new duration required
						if not self.right_live_durations:
							prime = self.new_duration(measure['style']['prime_durations'], measure['style']['prime_weights']) # Here, weights could be modified for "snap-fitting" preferences
							measure['right_durations'].append(prime)
							self.right_live_durations.append(prime)
						# Duration distribution - assignments to ['right_notes']
						for live_duration in self.right_live_durations:


						# Harmony insertion


						# Left
						if not self.left_live_durations:
							# Skew weights for left if "dragged"
							prime = self.new_duration(measure['style']['prime_durations'], measure['style']['prime_weights'])
							measure['left_durations'].append(prime)
							self.left_live_durations.append(prime)
						# Harmony insertion

						self.increment_count()

				self.count = 0

						# measure.music.append({'note_type': note_type, 'duration': duration, 'start_beat': start_beat, 'spn': spn, 'engraving_info': engraving_info})

	def new_duration(self, durations, weights):
		duration = random.choices(durations, weights)
		return {'name': duration[0], 'value': duration[1], 'remainder': duration[1], 'annotations': []}

	# increments durations, removes dead ones
	def increment_count(self):
		self.count += self.increment
		for live_duration in  + self.left_live_durations + self.right_live_durations:
			live_duration['life'] -= self.increment
			if not live_duration['life']:
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


