
"""
Static variables for formatting notation
"""

SHARP_LYNOTES = ['a,,,', 'ais,,,', 'b,,,', 'c,,', 'cis,,', 'd,,', 'dis,,', 'e,,', 'f,,', 'fis,,', 'g,,', 'gis,,', 'a,,', 'ais,,', 'b,,', 'c,', 'cis,', 'd,', 'dis,', 'e,', 'f,', 'fis,', 'g,', 'gis,', 'a,', 'ais,', 'b,', 'c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b', "c'", "cis'", "d'", "dis'", "e'", "f'", "fis'", "g'", "gis'", "a'", "ais'", "b'", "c''", "cis''", "d''", "dis''", "e''", "f''", "fis''", "g''", "gis''", "a''", "ais'''", "b''", "c'''", "cis'''", "d'''", "dis'''", "e'''", "f'''", "fis'''", "g'''", "gis'''", "a'''", "ais'''", "b'''", "c''''", "cis''''", "d''''", "dis''''", "e''''", "f''''", "fis''''", "g''''", "gis''''", "a''''", "ais''''", "b''''", "c'''''"]
FLAT_LYNOTES = ['a,,,', 'bes,,,', 'b,,,', 'c,,', 'des,,', 'd,,', 'ees,,', 'e,,', 'f,,', 'ges,,', 'g,,', 'aes,,', 'a,,', 'bes,,', 'b,,', 'c,', 'des,', 'd,', 'ees,', 'e,', 'f,', 'ges,', 'g,', 'aes,', 'a,', 'bes,', 'b,', 'c', 'des', 'd', 'ees', 'e', 'f', 'ges', 'g', 'aes', 'a', 'bes', 'b', "c'", "des'", "d'", "ees'", "e'", "f'", "ges'", "g'", "aes'", "a'", "bes'", "b'", "c''", "des''", "d''", "ees''", "e''", "f''", "ges''", "g''", "aes''", "a''", "bes''", "b''", "c'''", "des'''", "d'''", "ees'''", "e'''", "f'''", "ges'''", "g'''", "aes'''", "a'''", "bes'''", "b'''", "c''''", "des''''", "d''''", "ees''''", "e''''", "f''''", "ges''''", "g''''", "aes''''", "a''''", "bes''''", "b''''", "c'''''"]

SHARP_OCTAVE = ["C", "C♯", "D", "D♯", "E", "F", "F♯", "G", "G♯", "A", "A♯", "B"]
FLAT_OCTAVE = ["C", "D♭", "D", "E♭", "E", "F", "G♭", "G", "A♭", "A", "B♭", "B"]



LY_BLOCK_1 = """upper = {
  \\clef treble
  \\key c \\major
  \\time 4/4

"""
LY_BLOCK_2 = """
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
"""