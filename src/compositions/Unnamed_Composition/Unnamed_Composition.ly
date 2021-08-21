upper = {
    \clef treble
    \key f \minor
    \time 4/4

e'2. a'4 
d'4 a'2. 
g'4 e'2 a'4 
d'4 e'2. 
f'4 d'2 e'4 
f'8 b'8 f'4 c'4 g'4 
c'2 c'4 f'4 
b'2. c'4 
e'4 b'8 e'8~ e'8 e'8~ e'4 
a'8 c'8 g'8 c'16. d'32~ d'4 f'16. a'8 e'32 
e'16 c'16 a'16. a'32 g'2 e'8.. g'32 
b'8.. g'32~ g'8.. f'32 e'2 
d'4 g'8.. f'32~ f'16. f'8 f'32~ f'32 d'64 f'64~ f'8. 
e'8~ e'32. f'64 d'16~ d'8~ d'32. d'64~ d'16~ d'32. c'64~ c'8. g'32. g'8 e'64 c'16 
g'4 f'8~ f'32. c'64~ c'16~ c'8 d'32. g'64 g'16 f'32. e'8 e'64 e'16 
}

lower = {
    \clef bass
    \key f \minor
    \time 4/4

g16 c8 f16 b8 f8 f4. e8 
c1 
f4 c8 c8 g8 g8 g4 
f4 d2 a16. e32~ e8 
f2 b16. g32~ g8 g16. e32 d8 
g16. g32 f8~ f16. e16 b16.~ b32 d8.. e4 
e32 f8..~ f4~ f32 e16. c8~ c8 g8 
e8 a8~ a16 e8.~ e16 e8.~ e16 d8 g16 
c2 f8. d16 b16 f8. 
c4~ c16 a8.~ a8. a16~ a16 a8 a16 
a16 g8.~ g4~ g16 d8. c16 g8 f16 
b2 e8. a32 g32~ g16. e8 c32 
e16. d32 b8 a4~ a16. d32 e8~ e8.. f32 
e32 g8.. g8~ g32 d16.~ d8~ d32 f16. d4 
a32 d8 b16.~ b2 c8~ c32 f16. 

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
