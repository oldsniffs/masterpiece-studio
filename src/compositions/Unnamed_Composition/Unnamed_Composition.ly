upper = {
  \clef treble
  \key c \major
  \time 4/4

e'8 g'8 g'8 d'8 g'4 f'8 b'8 
a'8 d'8 e'4 b'4 e'4 
a'2. f'4 
a'2. e'64 b'8 b'16.. 
b'16 e'64 c'16 g'16..~ g'2~ g'8 a'64 a'16 g'32. 
f'16 e'64 c'32.~ c'8~ c'16 c'64 c'32.~ c'8~ c'16~ c'64 e'32.~ e'8 a'16 d'64 a'8 e'32. 
c'32. e'64~ e'8. a'32. f'64~ f'8.~ f'4~ f'32. e'16. d'16.. 
f'4 f'8 c'64 d'16.. b'2 
f'8 e'64 c'16..~ c'8 a'64 a'16.. c'8 f'64 e'16..~ e'64 f'16 d'8 e'32. 
d'8 e'64 a'16..~ a'8 b'64 g'16..~ g'4~ g'8 b'64 d'16.. 
g'2.~ g'8 c'64 e'16.. 
c'64 e'32 d'64 g'8.~ g'32. b'64~ b'8. g'8 g'32. f'64 g'16~ g'32. c'8 d'64~ d'16 
b'8~ b'32. d'32 a'32.~ a'2. 
c'8.~ c'64 d'32. b'8. c'64 e'32. g'64 e'64~ e'8..~ e'4 
b'1 

}

lower = {
  \clef bass
  \key c \major
  \time 4/4

a2 a4 b4 
a2 g8 g8 e8 c8 
d4 f4 g8 e16 e16~ e4 
f2~ f8. a16 a4 
g4.. e16 f16 a8. b16 f8 e16 
a16 d8 f16~ f4.. b16~ b16 c8 d16 
e16 f8.~ f16 b8. g16 g8.~ g16 d8. 
e4~ e16 g8.~ g16 c8.~ c16 e8 b16 
f8. a16 d8. g16~ g8. e16~ e4 
e16 c8. b4 g16 d16 b8~ b4 
f8 f8 g2. 
f8 g16 e16~ e8 a8~ a2 
d8 c8 b2 d4 
e4 g4 c2 
g8 b16. g32~ g4~ g8.. d32~ d4 

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
