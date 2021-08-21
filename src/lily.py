from custom_logging import *
import os
import subprocess

"""
Static variables and output functions for formatting notation
"""

SHARP_OCTAVE = ["C", "C♯", "D", "D♯", "E", "F", "F♯", "G", "G♯", "A", "A♯", "B"]
FLAT_OCTAVE = ["C", "D♭", "D", "E♭", "E", "F", "G♭", "G", "A♭", "A", "B♭", "B"]


# Lilypond

SHARP_PITCHES = ['a,,,', 'ais,,,', 'b,,,', 'c,,', 'cis,,', 'd,,', 'dis,,', 'e,,', 'f,,', 'fis,,', 'g,,', 'gis,,', 'a,,', 'ais,,', 'b,,', 'c,', 'cis,', 'd,', 'dis,', 'e,', 'f,', 'fis,', 'g,', 'gis,', 'a,', 'ais,', 'b,', 'c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b', "c'", "cis'", "d'", "dis'", "e'", "f'", "fis'", "g'", "gis'", "a'", "ais'", "b'", "c''", "cis''", "d''", "dis''", "e''", "f''", "fis''", "g''", "gis''", "a''", "ais'''", "b''", "c'''", "cis'''", "d'''", "dis'''", "e'''", "f'''", "fis'''", "g'''", "gis'''", "a'''", "ais'''", "b'''", "c''''", "cis''''", "d''''", "dis''''", "e''''", "f''''", "fis''''", "g''''", "gis''''", "a''''", "ais''''", "b''''", "c'''''"]
FLAT_PITCHES = ['a,,,', 'bes,,,', 'b,,,', 'c,,', 'des,,', 'd,,', 'ees,,', 'e,,', 'f,,', 'ges,,', 'g,,', 'aes,,', 'a,,', 'bes,,', 'b,,', 'c,', 'des,', 'd,', 'ees,', 'e,', 'f,', 'ges,', 'g,', 'aes,', 'a,', 'bes,', 'b,', 'c', 'des', 'd', 'ees', 'e', 'f', 'ges', 'g', 'aes', 'a', 'bes', 'b', "c'", "des'", "d'", "ees'", "e'", "f'", "ges'", "g'", "aes'", "a'", "bes'", "b'", "c''", "des''", "d''", "ees''", "e''", "f''", "ges''", "g''", "aes''", "a''", "bes''", "b''", "c'''", "des'''", "d'''", "ees'''", "e'''", "f'''", "ges'''", "g'''", "aes'''", "a'''", "bes'''", "b'''", "c''''", "des''''", "d''''", "ees''''", "e''''", "f''''", "ges''''", "g''''", "aes''''", "a''''", "bes''''", "b''''", "c'''''"]

# Note mirroring list of duration notations
LY_NOTE_NOTATIONS = [
    "1",
    "2",
    "4",
    "8",
    "16",
    "32",
    "64",
    "1.",
    "2.",
    "4.",
    "8.",
    "16.",
    "32.",
    "64.",
    "1..",
    "2..",
    "4..",
    "8..",
    "16..",
    "32..",
    "64..",
]

LY_BLOCK_1 = """upper = {
    \\clef treble
    """

LY_BLOCK_1_OLD = """upper = {
  \\clef treble
  \\key bes \\major
  \\time 4/4
 
"""  # move newline to BLOCK_2?

LY_BLOCK_2 = """}

lower = {
    \\clef bass
    """

LY_BLOCK_2_OLD = """
}

lower = {
  \\clef bass
  \\key c \\major
  \\time 4/4

"""
LY_BLOCK_3 = """
}

\\score {
  \\new PianoStaff <<
    \\set PianoStaff.instrumentName = #"Piano  "
    \\new Staff = "upper" \\upper
    \\new Staff = "lower" \\lower
  >>
\\layout { }
\\midi { }
}
"""

class Lily:
    def __init__(self, composition):
        self.composition = composition

    def output(self):
        log_header(f"Beginning lilypond output process")

        right_lynotation, left_lynotation = self.extract_lynotation()
        right_lymusic, left_lymusic = self.write_lymusic(right_lynotation, left_lynotation)

        log_debug(f"right_lymusic: {right_lymusic}")

        ly = self.format_ly(right_lymusic, left_lymusic)
        log_header(f"complete ly to write:")
        log_info(ly)
        self.write_ly(ly)
        self.run_lilypond(self.composition.filename)

    # Prepares lynotation from composition.segments
    # TODO: order methods by what uses what
    # separated by lilypond measure dividers: "|"
    # Presumably it is better to build lists to combine into strings, than rebuilding strings for each addition
    def extract_lynotation(self):
        left_lynotation = []
        right_lynotation = []

        for segment in self.composition.segments:
            for measure in segment['measures']:
                log_debug(measure['right_music'])
                measure_left_lynotation = []
                measure_right_lynotation = []
                for note in measure['right_music']:
                    measure_right_lynotation.append(f"{self.note_to_ly(note)}")
                measure_right_lynotation.append("\n")
                for note in measure['left_music']:
                    measure_left_lynotation.append(f"{self.note_to_ly(note)}")
                measure_left_lynotation.append("\n")
                right_lynotation.append(measure_right_lynotation)
                left_lynotation.append(measure_left_lynotation)
                log_debug(
                    f"from measure {measure['number']} right_music extracted ly music: {measure_right_lynotation}")
                log_debug(f"from measure {measure['number']} left_music extracted ly music:  {measure_left_lynotation}")
        return right_lynotation, left_lynotation

    def note_to_ly(self, note):
        tie = ""
        lypitch = self.spn_to_ly(note['spn'])
        lynote = self.beat_value_to_ly(note)
        if "tie" in note['engraving']:
            tie = "~"
        return f"{lypitch}{lynote}{tie}"

    # spn_to_ly is up with range ui methods
    def beat_value_to_ly(self, note):
        return LY_NOTE_NOTATIONS[note['masterpiece_index']]

    def write_lymusic(self, right_lynotation, left_lynotation):
        right_lymusic = []
        left_lymusic = []
        for measure in right_lynotation:
            right_lymusic.append(" ".join(measure))
        for measure in left_lynotation:
            left_lymusic.append(" ".join(measure))
        right_lymusic = "".join(right_lymusic)
        left_lymusic = "".join(left_lymusic)
        return right_lymusic, left_lymusic

    # prepares string
    def format_ly(self, right_lymusic, left_lymusic):
        return LY_BLOCK_1 + self.ly_keysig() + self.ly_timesig() + right_lymusic + LY_BLOCK_2 + self.ly_keysig() + self.ly_timesig() + left_lymusic + LY_BLOCK_3

    def ly_keysig(self):
        return f"\\key {self.composition.keysig_pitch} \\{self.composition.keysig_scale}\n    "

    def ly_timesig(self):
        return f"\\time {self.composition.timesig}\n\n"

    def spn_to_ly(self, spn):
        ly = spn[0].lower() # start with pitch

        if "♯" in spn:  # add accidental
            ly.append("is")
        elif "♭" in spn:
            ly.append("es")

        octave = int(spn[-1])  # for each octave above or below 3 (middle octave), add "'" or ","
        while octave != 3:
            if octave < 3:
                ly += ","
                octave += 1
            else:
                ly += "'"
                octave -= 1
        return ly

    # writes string to .ly file
    def write_ly(self, ly):
        if not os.path.exists(self.composition.filepath):
            os.makedirs(self.composition.filepath)
        file = open(f"{self.composition.filename}.ly", 'w')
        file.write(ly)
        file.close()

    # Runs Lilypond on given filepath
    def run_lilypond(self, filename):
        working_directory = os.getcwd()
        os.chdir(f"{self.composition.filepath}\\")
        log_debug(
            f"Attempting to call lilypond on {self.composition.file_namebase}.ly from cwd {os.getcwd()}\\")
        subprocess.call(["lilypond", f"{self.composition.file_namebase}.ly"])
        os.chdir(working_directory)
