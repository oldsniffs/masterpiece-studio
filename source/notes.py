"""
Purpose: Generate "notesets" for Rhythm class

The function "noteset" takes a timesig returns a skeleton dictionary of note dictionaries. It is called by the Rhythm class
in rhythm.py
Note dictionaries hold musical information about the note in the context of the song and may be modified dynamically
in the case of change in timesig


Static Assets:

Note Tuple Lists


"""

from custom_logging import *

# [(name, beats per note in */4 time)]
CoreNotes = [
	("whole", 4),
	("half", 2),
	("quarter", 1),
	("eighth", .5),
	("sixteenth", .25),
	("thirty-second", .125),
	("sixty-fourth", .0625)
]

DottedNotes = [
	("d-whole", 6),
	("d-half", 3),
	("d-quarter", 1.5),
	("d-eighth", .75),
	("d-sixteenth", .375),
	("d-thirty-second", .1875),
	("d-sixty-fourth", .09375),
]

DoubleDottedNotes = [
	("dd-whole", 7),
	("dd-half", 3.5),
	("dd-quarter", 1.75),
	("dd-eighth", .875),
	("dd-sixteenth", .4375),
	("dd-thirty-second", .21875),
	("dd-sixty-fourth", .109375),
]

AllNotes = CoreNotes+DottedNotes+DoubleDottedNotes

# ? Is it better that functions add items, or function returns the value for the new item?
# return "noteset" dictionary for rhythms.Rhythm


#
def noteset(timesig):
	noteset = {}
	log_info(f'Building noteset for {timesig[0]/timesig[1]} time', header="noteset")
	for note in AllNotes:
		noteset['beat value'] = beat_value(note[1], timesig[1])
		log_info(f'beat value for {note[0]} note in this time is {noteset["beat value"]}')


# move to rhythm.py
# don't think so
def beat_value(note_beats, timesig_den):
	return note_beats * timesig_den / 4

def is_appropriate(beat_value):
	#
	pass



if __name__ == "__main__":
	test_timesig = (4,4)
	test_noteset = noteset(test_timesig)