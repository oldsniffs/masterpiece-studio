upper = {
  \clef treble
  \key c \major
  \time 4/4

e'32 e'8..~ e'2~ e'32 e'8.. 
e'2~ e'32 e'8..~ e'4 
e'32 e'8..~ e'8~ e'32 e'16.~ e'8~ e'32 e'16.~ e'8~ e'32 e'16. 
e'8~ e'32 e'16.~ e'32 e'8..~ e'32 e'8..~ e'32 e'16 e'32~ e'8 
e'2.~ e'16. e'32~ e'8 
e'16. e'32~ e'8~ e'16. e'32~ e'8~ e'4~ e'16. e'32~ e'8 
e'16. e'32~ e'8~ e'16. e'32~ e'8~ e'16. e'32 e'8~ e'4 
e'4. e'8~ e'4. e'8 
e'8 e'8~ e'8 e'8~ e'8 e'8~ e'4 
e'8 e'8~ e'4. e'16. e'32~ e'4 
e'8.. e'32~ e'2. 
e'8.. e'32~ e'32 e'8..~ e'2 
e'32 e'16 e'32~ e'8~ e'2. 
e'16. e'32~ e'8~ e'16. e'32~ e'8~ e'16. e'32~ e'8~ e'16. e'32~ e'8 
e'16. e'32~ e'8~ e'16. e'32~ e'8~ e'16. e'16 e'16.~ e'4 

}

lower = {
  \clef bass
  \key c \major
  \time 4/4

a4 a4 a16 a8 a16~ a4 
a4.. a16~ a2 
a2.~ a8. a32 a32 
a4~ a8.. a32~ a4~ a8.. a32 
a16. a32 a8 a8 a8~ a16 a8.~ a16 a8 a16 
a8. a16~ a16 a32 a32~ a8~ a32 a8..~ a4 
a1 
a32 a8..~ a2. 
a2~ a32 a8..~ a4 
a2~ a32 a8..~ a32 a16 a64 a64~ a8 
a2.~ a16.. a8 a64 
a8..~ a64 a64~ a32. a64~ a8.~ a4~ a32. a64~ a8. 
a4~ a32. a64~ a8.~ a32. a64~ a8.~ a4 
a32. a64~ a8.~ a4~ a32. a64~ a8.~ a4 
a4~ a32. a64~ a8.~ a32. a16 a64 a8~ a8 a8 

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
