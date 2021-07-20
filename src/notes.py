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

PRIME_NOTES = CORE_NOTES+DOTTED_NOTES


def beat_value(note_beats, timesig_den):
	return note_beats * timesig_den / 4


def convert_durations(durations, timesig_den):
	return [(d[0], beat_value(d[1], timesig_den)) for d in durations]


# gives prime_durations, dd durations, and all durations, given time signature
def duration_sheet(timesig_den):
	log_info(f'Building duration_sheet for */{timesig_den} time')
	prime_durations = convert_durations(PRIME_NOTES, timesig_den)
	dd_durations = convert_durations(DOUBLE_DOTTED_NOTES, timesig_den)
	return {'prime': prime_durations, 'dd': dd_durations, 'all': prime_durations + dd_durations}


# Segment-specific list of note dictionaries
# note: {"type": string, "duration": float, "prime": int, "pair": int, length: [length weight list]}
# length weight list: [list of int values of weights for pair lengths starting at 2]
def notesheet():
	return {}.update()


if __name__ == "__main__":
	print(duration_sheet(2))
