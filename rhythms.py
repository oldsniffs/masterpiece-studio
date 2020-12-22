"""
	Rhythm.rhythm is the object of interest. It is a list of measures. 
	Measures are dictionaries representing each measure, with "right" and "left" holding lists of duration dictionaries.
	Duration dictionaries contain a reference to the standard note. Examples of special handling flags:
		Chords - flag intended for pitches.Notation 
		Sequences

	Measures place flags in subsequent measures when special events are rolled./=8
	
	Rhythm.notes holds note dictionaries. Note dictionaries represent current status of standard musical notes in the context of the  
	song, particular the number of beats it counts for based on time signature. Note dictionaries recorded in "right" and "left" lists
	can hold extra engraving data.

	rhythms.Rhythm is filled in constructor in steps by methods:
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

All musical data up to this point is format independent. studio.Studio handles formats

"""



import random
from custom_logging import *
import notes


class Rhythm:
	def __init__(self, measures_count, timesig):

		self.song_timesig = timesig
		self.current_timesig = timesig
		self.update_increment()

		self.measures_count = measures_count	

		self.noteset = notes.noteset(self.current_timesig)

		# increment is smallest note beat value
		# increment can change because timesig can change
		self.increment = 1
		self.update_increment()
		
		self.rhythm = self.empty_rhythm()
		self.fill_rhythm()

	def update_increment(self):
		self.increment = self.current_increment()

	def current_increment(self):
		# increment = smallest beat count
		return increment

	def empty_rhythm(self):
		return [{f"number":n, "flags":[], "measure":[]} for n in range(1, self.measures_count+1)]

	def fill_rhythm(self):
		for m in self.rhythm:
			log_rhythm(f'Filling Measure {m["number"]}')
			self.fill_right(m)
			self.fill_left(m)

	def fill_right(self, measure):
		beat = 0
		while beat < self.current_timesig[0]:
			
			for f in 

			# increment beat 
			beat += self.increment


	def _note_from_beatvalue(self, beat_value):

		for v[]

		log_warning(f"The beat value {beat_value} was searched for and not found")


if __name__ == "__main__":
	rhythm = Rhythm(10, (3,4))