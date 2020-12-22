"""

"""



import random
from custom_logging import *

ALL_DURATION_NOTATIONS = ['1.', '1', '2.', '2', '4.', '4', '8.', '8', '16.', '16', '32.', '32', '64.', '64']
DURATION_WEIGHTS = [(6, 1), (4, 6), (3, 5), (2, 16), (1.5, 3), (1, 26), (.75, 3), (.5, 20), (.375, 4), (.25, 6), (.1875, 0), (.125, 2), (.09375, 0), (.0625, 1)]

FILLER_ONLY_DURATIONS = ['1..', '2..', '4..', '8..', '16..', '32..', '64..'] # God forbid 64.. is ever used
LH_MODIFIER = 1.6

PAIRING_DURATIONS = [.5, .25, .125, .0625]
PAIRING_LENGTHS = [1, 2, 3, 4, 5, 6, 7]
# Weights: [(chance/10 of pairing[length weights])]
PAIRING_WEIGHTS_OLD = [(2, [6, 2, 1, 0, 0, 0, 0]), (4, [1, 4, 2, 1, 0, 0, 0]), (9, [2, 6, 4, 2, 1, ]), (9, [2, 6, 4, 2, 2])]
PAIRING_WEIGHTS = [(2, [6, 0, 4, 0, 2, 0, 0]), (4, [7, 0, 5, 0, 1, 0, 0]), (9, [8, 0, 6, 0, 3, 0, 0]), (9, [10, 0, 8, 0, 6, 0, 2])]


SYNCING_THRESHOLD = 4

# Placeholders for user defined variables:
MEASURES = 16
TIME_SIGNATURE = (4, 4)



class Rhythm:
	def __init__(self, measures, timesig):

		self.measures = measures
		self.timesig = timesig

		self.all_durations = self.get_all_durations()
		log_durations(f"self.all_durations: {self.all_durations}\n", source = "- Rhythm init -")

		self.appropriate_durations = self.get_appropriate_durations()
		print(f"DISPLAYING self.appropriate_durations: {self.appropriate_durations}\n")

		self.whole_beat_durations = self.get_whole_beat_durations()

		print(f"DISPLAYING self.whole_beat_durations: {self.whole_beat_durations}\n")
		self.weights_list = self.get_weights()
		print(f"DISPLAYING self.weights_list: {self.weights_list}\n")

		self.pattern = []

		log_debug(f"pattern before fill_pattern()- {self.pattern}")

		self.fill_pattern()

		self.left_pattern, self.right_pattern = self.prepare_notation()

		log_debug(f"left pattern {self.left_pattern}")
		log_debug(f"right pattern {self.right_pattern}")


	def prepare_notation(self):
		left_pattern = []
		right_pattern = []
		m_count = 1
		for measure in self.pattern:
			right_pattern.append(f"M{m_count}")
			left_pattern.append(f"M{m_count}")
			for beat in measure.right_hand["pattern"]:
				for duration in beat:
					right_pattern.append(duration[0][0])
			for beat in measure.left_hand["pattern"]:
				for duration in beat:
					left_pattern.append(duration[0][0])
			right_pattern.append("|")
			left_pattern.append("|")
			m_count += 1
		return left_pattern, right_pattern

	def fill_pattern(self):
		right_carryover = 0
		left_carryover = 0
		right_pairing = []
		final_measure = False

		for measure in range(self.measures):
			if measure+1 == self.measures:
				final_measure = True

			self.pattern.append(Measure(measure+1, self.timesig, self.all_durations, self.appropriate_durations, self.whole_beat_durations, self.weights_list, right_carryover=right_carryover, left_carryover=left_carryover, right_pairing=right_pairing, final_measure=final_measure))

			# Should just pass the previous measure, new measure can unpack all this at init
			right_carryover, right_pairing = self.pattern[-1].right_hand["overflow"], self.pattern[-1].right_hand["leftover_pairing"]
			left_carryover, left_pairing = self.pattern[-1].left_hand["overflow"], self.pattern[-1].left_hand["leftover_pairing"]

	def display_hand_patterns(self):
		for measure in self.pattern:
			print(f"Measure {measure.number}")
			measure.display_hand_patterns()
			print(f"{measure.number} of {len(self.pattern)} printed")

	def get_all_durations(self):
		beat_values = self.generate_beat_value_list()
		all_durations = [bv for bv in beat_values if self.timesig[0]]
		all_durations = sorted(all_durations, key=lambda d: d[1])
		all_durations.reverse()
		return all_durations

	# appropriate = duration is not greater than the beats per measure or double-dotted
	def get_appropriate_durations(self):
		beat_values = self.generate_beat_value_list()
		return [bv for bv in beat_values if self.timesig[0] >= bv[1] and ".." not in bv[0]]

	# no decimal
	def get_whole_beat_durations(self):
		return [d for d in self.all_durations if float(int(d[1])) == d[1]] 

	def generate_beat_value_list(self):
		beat_values = []
		for d in ALL_DURATION_NOTATIONS+FILLER_ONLY_DURATIONS:

			if '..' in d:
				base_value = 1/int(d[:-2])
				beat_value = base_value * self.timesig[1] * 1.75
			elif '.' in d:
				base_value = 1/int(d[:-1])
				beat_value = base_value * self.timesig[1] * 1.5
			else:
				base_value = 1/int(d)
				beat_value = base_value * self.timesig[1]
			beat_values.append((d, beat_value))
		
		return beat_values

	# Proportion generation could well change with user feedback.
	# Does time signature matter? Are 1/8 notes more common in 6/8 than 3/4?
	# Should large notes be left appropriate, and allowed to form long tied carryovers? -> Yes, but weight should drop
	def get_weights(self):
		return [weight[1] for weight in [dw for dw in DURATION_WEIGHTS if dw[0] in [d[1] for d in self.appropriate_durations]]]


class Measure:
	def __init__(self, number, timesig, all_durations, appropriate_durations, whole_beat_durations, duration_weights, right_carryover=0, left_carryover=0, right_pairing=[], left_pairing=[], final_measure=False):
		# measure number for debugging
		self.number = number
		self.timesig = timesig
		self.beats_per_measure = timesig[0]
		self.final_measure = final_measure

		self.all_durations = all_durations
		self.appropriate_durations = appropriate_durations
		self.whole_beat_durations = whole_beat_durations

		# Patterns are lists of beats, 1 per bpm, and beats are lists of durations
		# Beat lists can be empty if previous duration is fully covering that beat
		# "hand" Dictionaries contain: side, pattern: carryover, pairing, list of beats (old pattern), weights, overflow, leftover pairing
		self.right_hand = {"side": "right", "carryover": right_carryover, "pairing": right_pairing, "pattern": [], "duration_weights": duration_weights}
		self.right_hand["overflow"], self.right_hand["leftover_pairing"] = self.fill_hand(self.right_hand)
		
		self.left_hand = {"side": "left", "carryover": left_carryover, "pairing": left_pairing, "pattern": [], "duration_weights": self.modify_weights_for_lh()}
		# self.syncs is list of tuples: (duration tuple, measure count)
		self.sync_markers = self.get_sync_markers()
		self.syncs = self.get_syncs()
		self.matched_syncs = [] # For debugging
		self.left_hand["overflow"], self.left_hand["leftover_pairing"] = self.fill_hand(self.left_hand)

	def modify_weights_for_lh(self):
		# "midpoint" should use weight value as well as index
		lh_weights = []
		midpoint = int(len(self.right_hand["duration_weights"])/2)
		modifier = 1
		for i in range(len(self.right_hand["duration_weights"])):
			if i < midpoint:
				modifier = LH_MODIFIER
			lh_weights.append(self.right_hand["duration_weights"][i]*modifier)
		return lh_weights

	def display_hand_patterns(self):
		for h in [self.right_hand, self.left_hand]:
			print(f"Displaying {h['side']}")
			for b in h["pattern"]:
				count = 0
				for d in [d for d in b if d[0][0] != "|"]:
					print(f"{d[0][0]}", end=" ")
					count += d[0][1]
				print(f" /  --> {count}")
			print(f'Overflow beats: {h["overflow"]}')


	def get_carryovers(self):
		return right_carryover, left_carryover

	# For left hand, check each beat (or duration, by count) to see if right hand has a duration inserted. Roll a chance to copy that duration
	# For left hand, run the weights through a modifier to weight towards longer durations
	def fill_hand(self, hand):

		if self.final_measure == True:
			print(f"LOG: === FINAL MEASURE ===")
		print(f"LOG: ====== Starting fill of measure {self.number}, {hand['side']} hand pattern ======")

		pattern = hand["pattern"]
		pairing = hand["pairing"]
		carryover = hand["carryover"]
		filled_beats = 0
		if hand['side'] == 'left':
			syncs = self.syncs.copy()

		for beat in range(self.beats_per_measure):
			new_beat = []
			count = 0 # Floatable beat count within beat

			if beat > 0:
				print(f"LOG: ------ Starting beat {beat+1} with {carryover} carryover and {filled_beats} filled beats. Count reset to {count} ------")

			if filled_beats:
				print(f"LOG (filled_beats): {filled_beats} filled_beats left. Appending empty beat list")
				pattern.append(new_beat)
				print(f"LOG (filled_beats): {new_beat} appended to measure --> {pattern}")
				filled_beats -= 1
				continue
		
			# Change to elif?
			if carryover:

				if carryover < 1:
					new_duration, carryover_count = self.fill_small_carryover(carryover, new_beat)
					count += carryover_count
					carryover -= (new_duration[1] + carryover_count)

				else:
					print(f"LOG: Carryover {carryover} >= 1")
					biggest_whole = float(int(carryover))
					new_duration, whole_carryover = self.get_filled_beats_spawn(biggest_whole, pattern)
					carryover -= new_duration[1]
					filled_beats = new_duration[1]-1
					if carryover:
						new_duration = (new_duration[0]+"~", new_duration[1])
					print(f"LOG: Carryover {carryover} filled {filled_beats}")

				print(f"LOG: Appending new_duration {new_duration} to new_beat at count {count}")
				new_beat.append(((new_duration), count))
				count+=new_duration[1]

			while count < 1:

				if pairing:
					print(f"LOG: Pairing detected: {pairing}")
					new_duration = pairing[0]
					pairing[1] -= 1

					# If there is a sync, and this pairing would pass sync mark, halt pairings
					if hand['side'] == 'left' and syncs:
						if len(pattern)+count + new_duration[1] > syncs[0][1]:
							print(f"DEBUG: Pairing passes sync mark for {syncs[0]}. Halting pairings")
							pairing = []
							continue

					# Count is over, clear list
					if not pairing[1]:
						print("LOG: End of pairing")
						pairing = []
					print(f"LOG: Appending PAIRED new_duration {new_duration} to new_beat at beat count {count}")
					new_beat.append(((new_duration), count))
					count += new_duration[1]
					continue

				# Left hand virgin should not cross sync marker
				if hand["side"] == "left":
					
					beat_limit = None
					if syncs:
						print(f"DEBUG: Current count: beats {len(pattern)}, count {count}. Next sync: {syncs[0]}")
						if count+len(pattern) == syncs[0][1]:
							virgin_duration = syncs[0][0]
							print(f"LOG(Syncing): Sync marker reached. syncs[0] {syncs[0]} chosen as virgin {virgin_duration}")
							self.matched_syncs.append(syncs[0])
							del(syncs[0])
						else:							
							beat_limit = syncs[0][1]-(len(pattern)+count)
					
							virgin_duration = self.get_random_duration(hand["duration_weights"], beat_limit=beat_limit)
							print(f"LOG: Virgin selected --> {virgin_duration} at count {count}")
					else:
						virgin_duration = self.get_random_duration(hand["duration_weights"], beat_limit=beat_limit)
						print(f"LOG: Virgin selected --> {virgin_duration} at count {count}. No syncs detected")

				else:
					virgin_duration = self.get_random_duration(hand["duration_weights"])
					print(f"LOG: Virgin selected --> {virgin_duration} at count {count}")

				# virgin is suitable, becomes new_duration
				if count + virgin_duration[1] <= 1:
					new_duration = virgin_duration
					pairing = self.check_pairing(new_duration, count)

				elif count == 0 and virgin_duration[1] % 1 == 0:
					for duration in [d for d in self.whole_beat_durations if d[1] + len(pattern) <= self.beats_per_measure]:
						if duration[1] == virgin_duration[1]:
							new_duration = duration
							filled_beats = new_duration[1]-1
							print(f"LOG(==): {duration} selected as biggest available whole beat duration.")
							break
						elif duration[1] < virgin_duration[1]:
							new_duration = duration
							carryover = virgin_duration[1] - new_duration[1]
							filled_beats = new_duration[1]-1
							print(f"LOG(<): {duration} selected as biggest available whole beat duration. Carryover: {carryover}")

				else:
					print(f"LOG: Virgin OVERFLOWS by {virgin_duration[1]-(1-count)}")
					new_duration = self.complete_beat(1-count, new_beat, count)
					carryover = virgin_duration[1]-(1-count)
					count += (1-count)-new_duration[1]

				print(f"LOG: Appending new_duration {new_duration} to new_beat at count {count}")
				new_beat.append(((new_duration), count))
				count+=new_duration[1]

			print(f'LOG: Count {count} reached for beat {len(pattern)+1}. Appending to {hand["side"]}_hand pattern with {filled_beats} filled_beats and {carryover} carryover')
			pattern.append(new_beat)

		print(f"LOG: End of Measure reached. Returning {carryover} carryover OR converting {filled_beats} filled_beats for right_carryover variable")

		carryover += filled_beats
		print(f"DEBUG: carryover {carryover}")
		if self.final_measure == True and carryover:
			print(f"DEBUF: Removing tie")
			self.remove_tie_if_final(pattern)

		return carryover, pairing

	def get_syncs(self):
		mark_index = 0
		markers = self.sync_markers
		syncs = []
		print(f"DEBUG: Filling syncs from markers list: {markers}")
		for mark in markers:
			if mark[0]:
				syncs.append(mark)
			else:
				if len(markers) > mark_index + 1:
					print(f"DEBUG: Filling mark {mark} with another mark ahead at {markers[mark_index+1]}. Beat limit needed")
					beat_limit = markers[mark_index+1][1] - markers[mark_index][1]
					print(f"DEBUG: Beat limit determined {beat_limit}")
				else:
					beat_limit = None
				syncs.append((self.get_random_duration(self.left_hand["duration_weights"], beat_limit=beat_limit), mark[1]))
			mark_index += 1
		print(f"LOG(get_syncs): Syncs list {syncs} filled from markers {markers}")
		return syncs

	def get_sync_markers(self):
		markers = []
		b_count = 0
		duration = None
		for b in self.right_hand["pattern"]:
			for d in [d for d in b if d[0][1] > .125 and d[1]+len(self.left_hand["pattern"]) >= self.left_hand["carryover"]]:
				duration = None

				# If the last marker's sync duration does not cross this point in right hand, and syncing roll passes:

				if random.randint(1, 20) > 20 - SYNCING_THRESHOLD:

					# chance to match rh's duration
					if random.randint(0, 2) == 0:
						# give d's duration only, not the count
						duration = (d[0][0], d[0][1])
					markers.append((duration, b_count + d[1]))
			b_count += 1
		# Debuggin variable
		return markers

	def scout_next_sync(self, measure_count):
		if self.syncs:
			beats_until_sync = self.syncs[0][1] - measure_count
			print(f"DEBUG(scout_next_sync): syncs[0] detected: {syncs[0]}. measure_count {measure_count} - {syns[0][1]} = {beats_until_sync}")
			return beats_until_sync

	# Returns pairing list. empty if none
	def check_pairing(self, duration, count):

		if duration[1] in PAIRING_DURATIONS and self.check_beat_strength(duration, count) == True:
			pairing = self.get_pairing(duration)
			print(f"LOG(check_pairing): Pairing {pairing} created. Returning")
			return pairing


	def check_beat_strength(self, duration, count):
		print(f"LOG(check_beat_strength): Checking if a duration {duration} on count {count} is strong")
		if (count/duration[1]) % 2 == 0:
			print(f"LOG(check_beat_strength): STRONG")
			return True
		# Might not need this else
		else:
			print(f"LOG(check_beat_strength): WEAK")
			return False

	def get_pairing(self, duration):
		print(f"LOG(get_pairing): Getting pairing for {duration}")
		weights = PAIRING_WEIGHTS[PAIRING_DURATIONS.index(duration[1])]
		if random.randint(1, 10) < weights[0]:
			return [duration, random.choices(PAIRING_LENGTHS, weights[1])[0]]

	def remove_tie_if_final(self, pattern):
		for i in range(len(pattern)-1, 0, -1):
			if pattern[i]:
				pattern[i][-1] = ((pattern[i][-1][0][0][:-1], pattern[i][-1][0][1]), pattern[i][-1][1])

	def get_filled_beats_spawn(self, spawn_beats, pattern):
		# Appends with tie if no exact match, returns finisher for new_duration
		print(f"LOG(get_filled_beats_spawn): Seeking whole beat for spawn_beats {spawn_beats} + past beats {len(pattern)} <= beats_per_measure {self.beats_per_measure}")
		for duration in [d for d in self.whole_beat_durations if d[1] + len(pattern) <= self.beats_per_measure]:
			if duration[1] <= spawn_beats:
				print(f"LOG(get_filled_beats_spawn): {duration} selected. Returning with whole_carryover {spawn_beats-duration[1]}")
				return duration, spawn_beats-duration[1]

	def find_duration_by_beat_value(self, beat_value): # Use if you know match exists
		print(f"LOG(find_duration_by_beat_value): seeking duration for beat value {beat_value}")
		for duration in self.all_durations:
			if duration[1] == beat_value:
				return duration

	def complete_beat(self, remaining_beats, pattern, count):
		print(f"LOG(complete_beat): Completing beat, {remaining_beats} beats remaining")
		for duration in self.all_durations:
			if duration[1] == remaining_beats:
				print(f"LOG(complete_beat) {duration} matches {remaining_beats} remaining_beats. Returning")
				return (duration[0]+"~", duration[1])
			elif duration[1] < remaining_beats:
				print(f"LOG(complete_beat): appending {duration} towards {remaining_beats} remaining_beats")
				pattern.append(((duration[0]+"~", duration[1]), count))
				remaining_beats -= duration[1]
				count += duration[1]

	def fill_small_carryover(self, carryover, pattern):

		print(f"LOG(fill_small_carryover): Filling carryover at beat {len(pattern)} starting with {carryover} carryover beats. Attempting to fill")
		remaining_beats = carryover
		count = 0

		for duration in self.all_durations:
			if duration[1] == remaining_beats:
				print(f"LOG(fill_small_carryover) {duration} matches {remaining_beats} remaining_beats. Returning")
				return (duration[0], duration[1]), count
			elif duration[1] < remaining_beats:
				# if self.timesig[1] % duration[1]
				print(f"LOG(fill_small_carryover): {duration} found to fit in {remaining_beats}. Appending. {remaining_beats-duration[1]} beats remaining")
				pattern.append(((duration[0]+"~", duration[1]), count))
				remaining_beats -= duration[1]
				count += duration[1]

	def get_random_duration(self, weights, beat_limit=None):
		print(f"DEBUG: Getting random duration with beat limit {beat_limit}")
		if not beat_limit:
			return random.choices(self.appropriate_durations, weights)[0]
		else:
			limited_durations = self.appropriate_durations.copy()
			limited_weights = weights.copy()
			for ad in self.appropriate_durations:
				if ad[1] > beat_limit:
					del(limited_durations[0])
					del(limited_weights[0])
			return random.choices(limited_durations, limited_weights)[0]


if __name__ == "__main__":

	rhythm = Rhythm(6, (7,8))

	print(rhythm.right_pattern)
	rhythm.display_hand_patterns()
	for measure in rhythm.pattern:
		print(f"Measure {measure.number} syncs: {measure.syncs} from markers {measure.sync_markers}")
		print(f"Matched syncs used: {measure.matched_syncs}")
	print(f"left: {rhythm.left_pattern}")
	print(f"right: {rhythm.right_pattern}")
	print(f'durations list: {rhythm.appropriate_durations} {rhythm.weights_list}')
