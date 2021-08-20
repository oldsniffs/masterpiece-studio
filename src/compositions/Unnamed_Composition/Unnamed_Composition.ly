upper = {
  \clef treblec'4 d'4 e'2 
d'4 d'2 b'4 
e'4 g'8 f'8~ f'4. c'8 
f'1 
e'4 d'2 a'4 
d'4 e'16 b'8.~ b'4 a'16 f'8. 
e'4~ e'16 e'8.~ e'16 a'16. e'16 a'32~ a'8.. d'32 
e'16. c'32~ c'8 b'2 f'16. b'16 g'16. 
c'8 c'32 a'16.~ a'4~ a'8~ a'32 f'16.~ f'4 
g'8 a'32 b'16.~ b'8 e'32 d'16.~ d'8 f'32 g'16.~ g'4 
b'8 e'32 g'16.~ g'4 d'32 d'8.. b'4 
g'32 e'8 e'16.~ e'4~ e'8~ e'32 g'16. b'4 
e'32 a'8 a'16.~ a'8 g'32 a'16.~ a'16. b'8 c'32~ c'16. g'8 d'32 
d'8.. d'32~ d'16. e'32~ e'8~ e'16. g'32 a'8~ a'4 
d'16. f'8 d'32~ d'16. f'8 f'32~ f'16. b'8 c'32~ c'8.. b'32 

}

lower = {
  \clef bass
  \key c \major
  \time 4/4

c4 e32 d8 d16.~ d2 
a4 f8~ f32 b16.~ b4~ b8 d32 d16. 
b32 b16 d32~ d8~ d32 f8.. c2 
f2.~ f32 a32 f8. 
c16 c8. c4 a16 g8.~ g4 
f4~ f16 f8 g16~ g8. e16~ e8. a16 
e8. f16~ f8. c16 g8. d16~ d4 
g4.. a16~ a2 
a8. g16 f8 a8 d8 a8 b8 g8 
f16. a32 e8 f2 a16. c32 c8 
b4~ b16. f16 c16.~ c16. c16. b16 e16 b8. 
d16 c8. f2 f4 
a4 g2. 
a16. d32~ d8~ d16. a32 e8 f16. g32~ g8~ g16. d8 g32 
d2 c8.. b32 e4 

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
