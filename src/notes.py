from custom_logging import *

"""
Static variables for notes

The function "get_sheets" takes a timesig_den and returns ordered lists of duration values and note dictionaries
"""


PITCHES = ["A", "B", "C", "D", "E", "F", "G"]

SCALE_INTERVALS = {
	"major": [],
	"minor": [],
	"harmonic": [],
	"melodic": [],
	"major": [],
	"major": [],
	"major": [],
	"major": [],
	"major": [],
}


# Note Data
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

# Durations lists can expand, but beginning would still mirror note indices
PRIME_DURATIONS = CORE_NOTES + DOTTED_NOTES
ALL_MASTERPIECE_NOTES = PRIME_DURATIONS + DOUBLE_DOTTED_NOTES

# Note indices
PRIME_DURATIONS_INDEX = [i for i in range(len(PRIME_DURATIONS))]


def beat_value(note_beats, timesig_den):
	return note_beats * timesig_den / 4


def convert_durations(durations, timesig_den):
	return [(d[0], beat_value(d[1], timesig_den)) for d in durations]


# Returns data objects for durations and notes
def get_sheets(timesig_den):
	log_info(f'Building duration_sheet for */{timesig_den} time')

	# ordered list of prime duration values for durations
	duration_sheet = [beat_value(d[1], timesig_den) for d in PRIME_DURATIONS]

	# mirror ordered list of dicts for notes
	note_sheet = [{'masterpiece_index': n, 'name': ALL_MASTERPIECE_NOTES[n][0], 'beat_value':beat_value(ALL_MASTERPIECE_NOTES[n][1], timesig_den)} for n in range(len(ALL_MASTERPIECE_NOTES))]
	note_beat_values = [note['beat_value'] for note in note_sheet]
	note_sheet_ascending = sorted(note_sheet, key = lambda note: note['beat_value'])
	note_sheet_descending = note_sheet_ascending[::-1]

	log_debug(f"duration_sheet: {duration_sheet}")
	log_debug(f"note_sheet: {note_sheet}")

	return duration_sheet, note_sheet, note_beat_values, note_sheet_ascending, note_sheet_descending


if __name__ == "__main__":
	config_log()
	duration_sheet, note_sheet, note_beat_values, note_sheet_ascending, note_sheet_descending = get_sheets(4)
	print(note_sheet_descending)
	print(note_sheet)
	print(note_beat_values)
