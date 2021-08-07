from custom_logging import *

"""
Purpose: Generate "durations" for Rhythm class

The function "duration_sheet" takes a timesig returns a skeleton dictionary of note dictionaries. It is called by the Rhythm class
in rhythm.py

TODO: give increment an algorithm

"""
SHARP_LYNOTES = ['a,,,', 'ais,,,', 'b,,,', 'c,,', 'cis,,', 'd,,', 'dis,,', 'e,,', 'f,,', 'fis,,', 'g,,', 'gis,,', 'a,,', 'ais,,', 'b,,', 'c,', 'cis,', 'd,', 'dis,', 'e,', 'f,', 'fis,', 'g,', 'gis,', 'a,', 'ais,', 'b,', 'c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b', "c'", "cis'", "d'", "dis'", "e'", "f'", "fis'", "g'", "gis'", "a'", "ais'", "b'", "c''", "cis''", "d''", "dis''", "e''", "f''", "fis''", "g''", "gis''", "a''", "ais'''", "b''", "c'''", "cis'''", "d'''", "dis'''", "e'''", "f'''", "fis'''", "g'''", "gis'''", "a'''", "ais'''", "b'''", "c''''", "cis''''", "d''''", "dis''''", "e''''", "f''''", "fis''''", "g''''", "gis''''", "a''''", "ais''''", "b''''", "c'''''"]
FLAT_LYNOTES = ['a,,,', 'bes,,,', 'b,,,', 'c,,', 'des,,', 'd,,', 'ees,,', 'e,,', 'f,,', 'ges,,', 'g,,', 'aes,,', 'a,,', 'bes,,', 'b,,', 'c,', 'des,', 'd,', 'ees,', 'e,', 'f,', 'ges,', 'g,', 'aes,', 'a,', 'bes,', 'b,', 'c', 'des', 'd', 'ees', 'e', 'f', 'ges', 'g', 'aes', 'a', 'bes', 'b', "c'", "des'", "d'", "ees'", "e'", "f'", "ges'", "g'", "aes'", "a'", "bes'", "b'", "c''", "des''", "d''", "ees''", "e''", "f''", "ges''", "g''", "aes''", "a''", "bes''", "b''", "c'''", "des'''", "d'''", "ees'''", "e'''", "f'''", "ges'''", "g'''", "aes'''", "a'''", "bes'''", "b'''", "c''''", "des''''", "d''''", "ees''''", "e''''", "f''''", "ges''''", "g''''", "aes''''", "a''''", "bes''''", "b''''", "c'''''"]

SHARP_OCTAVE = ["C", "C♯", "D", "D♯", "E", "F", "F♯", "G", "G♯", "A", "A♯", "B"]
FLAT_OCTAVE = ["C", "D♭", "D", "E♭", "E", "F", "G♭", "G", "A♭", "A", "B♭", "B"]



# Durations
# [(name, beats per note in */4 time)]
CORE_NOTES = [
	("whole", 4),
	("half", 2),
	("quarter", 1),
	("eighth", .5),
	("sixteenth", .25),
	("thirtysecond", .125),
	("sixtyfourth", .0625)
]

DOTTED_NOTES = [
	("dwhole", 6),
	("dhalf", 3),
	("dquarter", 1.5),
	("deighth", .75),
	("dsixteenth", .375),
	("dthirtysecond", .1875),
	("dsixtyfourth", .09375),
]

DOUBLE_DOTTED_NOTES = [
	("ddwhole", 7),
	("ddhalf", 3.5),
	("ddquarter", 1.75),
	("ddeighth", .875),
	("ddsixteenth", .4375),
	("ddthirtysecond", .21875),
	("ddsixtyfourth", .109375),
]

PRIME_DURATIONS = CORE_NOTES + DOTTED_NOTES
ALL_NOTES = PRIME_DURATIONS + DOUBLE_DOTTED_NOTES

# Note indices
PRIME_DURATIONS_INDEX = [i for i in range(len(PRIME_DURATIONS))]


def beat_value(note_beats, timesig_den):
	return note_beats * timesig_den / 4


def convert_durations(durations, timesig_den):
	return [(d[0], beat_value(d[1], timesig_den)) for d in durations]


# Gives data objects for durations and notes
def get_sheets(timesig_den):
	log_info(f'Building duration_sheet for */{timesig_den} time')

	# return lists of tuples for prime durations
	duration_sheet = [beat_value(d[1], timesig_den) for d in PRIME_DURATIONS]

	# same list converted to dicts for notes
	note_sheet =  [{'type': note[0], 'value':beat_value(note[1], timesig_den)} for note in ALL_NOTES]

	return duration_sheet, note_sheet


if __name__ == "__main__":
	duration_sheet, note_sheet = get_sheets(4)
	print(duration_sheet)
	print(note_sheet)
