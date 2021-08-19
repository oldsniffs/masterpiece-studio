upper = {
  \clef treble
  \key c \major
  \time 4/4

f'2 d'4 d'4 
e'4 d'4 b'8 e'8 g'4 
e'4 a'16. d'8 e'32~ g'8~ d'32 c'16.~ c'4 
a'32 e'8 f'16.~ e'4~ b'8~ f'32 e'16.~ a'4 
g'8~ a'32 g'16.~ b'32 c'8..~ b'2 
b'4~ b'32 c'8..~ f'4~ g'32 b'8.. 
f'4~ a'32 b'8..~ f'2 
e'32 b'8..~ g'2. 
c'2~ b'32 a'32 a'8 b'16~ g'4 
a'8. f'16~ f'8. c'16~ a'4.. f'16 
b'4.. b'16~ e'2 
a'4.. g'16~ c'8. b'16~ g'4 
g'16 e'8.~ e'16 f'16 g'8~ c'2 
g'8 d'8~ d'8 b'8~ e'8 e'8 g'4 
a'4 d'4 c'2 

}

lower = {
  \clef bass
  \key c \major
  \time 4/4

b16 d8.~ c16 b8.~ e4~ a16 b8. 
c4~ f16 a8 b16~ c8. e16~ g16 c8. 
d16 a8 c16~ a8 e8 d2 
f2. a8 f8 
g8 b8 e4 a8 d8 f8. f16 
d4.. a16~ d2 
a8. g16 b2. 
a4 c8 e16. g32~ g8.. f32~ a4 
e2~ g8.. c32~ c8.. g32 
d16. f32~ d8~ g16. g32~ c8~ f16. c8 g32~ d4 
f2~ a8.. d32~ b4 
a8.. f32~ a4~ e8.. f32~ d4 
g2~ d8.. b32~ d4 
a16. c32~ c8~ c32 d8..~ a4~ d32 b8 f16. 
g2.~ d8~ a32 e16. 

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
