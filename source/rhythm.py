"""
Purpose:

Contains Rhythm class, instances of which are used by composition.py as the rhythmic base to build a song from.

Measures are dictionaries representing each measure, with "right" and "left" holding lists of duration dictionaries.
Duration dictionaries contain a reference to the standard note. Examples of special handling flags:
	Chords - flag intended for pitches.Notation
	Sequences

Measures place flags in subsequent measures when special events are rolled./=8

Rhythm.notes holds note dictionaries. Note dictionaries represent current status of standard musical notes in the context of the
song, particular the number of beats it counts for based on time signature. Note dictionaries recorded in "right" and "left" lists
can hold extra engraving data.

rhythm.Rhythm is filled in constructor in steps by methods:
	mark_phases - plants phase change flag in
	fill_rhythm


measure dictionary {
	number:
	flags: list of flag strings
	right: list of right hand duration dictionaries  	_ same size
	left: list of left hand duration dictionaries		/
}

duration dictionary {
	note: string, refering to a note dictionary
	flags: list of flag strings
}

note dictionary {
	type: string "whole"
}

Up to this point, and until a all musical data is format-neutral. Formatting is done by studio.Studio

"""

from source.custom_logging import *
from source import notes


class Measure:
	def __init__(self, number):
		self.number = number
		self.event_markers

# The train chugs here
class Rhythm:
	def __init__(self, segments):

		# segments:  (active_measure, timesig, )
	### static song state attributes
		self.segments = segments

		self.starting_timesig = segment[]
		self.measure_count = measure_count
		self.song_timesig = timesig

	### dynamic song state attributes
		self.current_timesig = timesig
		self.update_increment()

		self.

		self.noteset = notes.noteset(self.current_timesig)

		# increment is smallest note beat value
		# increment can change because timesig can change
		self.increment = 1
		self.update_increment()

		# pattern is a sequential list of all measures
		self.pattern = self.empty_pattern()
		self.fill_pattern()

	def update_increment(self):
		self.increment = self.current_increment()

	def current_increment(self):
		# increment = smallest beat count
		increment = .1
		return increment

	def empty_pattern(self):
		return [{"number":n, "flags":[], "measure":[]} for n in range(1, self.measure_count+1)]

	def fill_pattern(self):
		for m in self.pattern:
			log_rhythm(f'Filling Measure {m["number"]}')
			self.fill_right(m)
			self.fill_left(m)

	def fill_right(self, measure):
		pass
		beat = 0

	def fill_left(self, measure):
		pass
		beat = 0

	def fill_


	def _note_from_beatvalue(self, beat_value):

		log_warning(f"The beat value {beat_value} was searched for and not found")


if __name__ == "__main__":
	rhythm = Rhythm(10, (3, 4))
	print(rhythm.pattern)