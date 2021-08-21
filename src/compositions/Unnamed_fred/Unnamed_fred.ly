upper = {
    \clef treble
    \key f \minor
    \time 4/4

d'2 d'4 g'32 e'8.. 
e'2~ e'32 b'8..~ b'4 
a'32 c'8.. d'4 d'32 a'8.. c'4 
b'32 c'8.. a'32 g'8 e'16.~ e'8 a'32 c'16. c'32 d'8.. 
f'8 c'32 e'16.~ e'2~ e'8~ e'32 a'16. 
e'8~ e'32 g'16.~ g'8 f'32 e'16. c'2 
b'4~ b'8 d'32 e'16.~ e'8~ e'32 d'16. b'4 
a'8~ a'32 d'16. d'16. f'32 f'8 d'16. e'8 e'32~ e'4 
c'8.. b'32 g'16. a'32~ a'8~ a'2 
e'4 a'16. c'32 c'8~ c'4 f'16. c'32~ c'8 
f'16. c'8 c'32~ c'4~ c'8.. e'32~ e'16. g'16 d'16. 
f'8 f'32 g'16. b'4~ b'8 c'32 b'16. f'32 c'8 c'16. 
c'8~ c'32 g'16.~ g'32 g'8..~ g'32 d'8.. d'4 
d'2 d'32 d'8 c'16.~ c'8~ c'32 b'16. 
f'8 b'32 b'16. b'2 b'16 d'8. 
}

lower = {
    \clef bass
    \key f \minor
    \time 4/4

d8. c16~ c4.. c16 g8 b8 
e8 c8~ c8 e16 b16 c16 e8 a16~ a8. b16 
a4.. g16 a8. b16~ b8. b16 
a2~ a8. d16 b4 
d4.. e16~ e4.. b16 
b8 b8~ b4. a8 a4 
c2 d8 c8 d16 b8 e16 
b2. a8. e16 
g4.. a16~ a4.. d16 
a2. g8. b16 
e64 f64~ f8.. a64 d64 e8..~ e64 a64~ a8..~ a64 b64~ b8.. 
b64 c64~ c8.. a2. 
a2~ a64 e8 d16..~ d64 g64 b8.. 
b64 f8 g16..~ g64 g8 a16..~ a4~ a8~ a64 e32 d64~ d16 
f4 a8 d32. f64 a16~ a8~ a32. a64~ a16 c4 

}

\score {
  \new PianoStaff <<
    \set PianoStaff.instrumentName = #"Piano  "
    \new Staff = "upper" \upper
    \new Staff = "lower" \lower
  >>
\layout { }
\midi { }
}
