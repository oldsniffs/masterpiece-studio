"""
LY_BLOCKs are used .ly notation
"""

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