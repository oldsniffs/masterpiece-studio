upper = {
  \clef treble
  \key c \major
  \time 4/4

e'2 e'2 
e'4 e'2. 
e'4 e'4 e'32 e'8 e'16.~ e'32 e'8.. 
e'32 e'8..~ e'32 e'8 e'16.~ e'4~ e'8~ e'32 e'16. 
e'2~ e'8~ e'32 e'16. e'4 
e'4 e'4 e'2 
e'2 e'8 e'8 e'4 
e'4 e'4. e'4. 
e'8 e'2.. 
e'8 e'8~ e'4. e'4. 
e'8 e'8 e'2 e'8 e'8 
e'4 e'2 e'4 
e'4 e'16. e'8 e'32~ e'16 e'32 e'32~ e'8~ e'16. e'8 e'32 
e'8.. e'32~ e'8~ e'32 e'16.~ e'32 e'8..~ e'32 e'8.. 
e'32 e'8..~ e'4~ e'32 e'32 e'8.~ e'16 e'8. 

}

lower = {
  \clef bass
  \key c \major
  \time 4/4

a8 a8~ a16 a8.~ a16 a8 a4~ a16 
a2~ a8. a4~ a16 
a2~ a8. a16 a4 
a2. a8 a8 
a8 a8~ a8 a16 a16~ a8. a16~ a8. a16 
a8. a16~ a8. a16~ a4.. a16 
a2~ a8. a16~ a16 a8 a16 
a8. a16~ a4.. a16~ a16 a8. 
a4~ a16 a2~ a8. 
a4~ a16 a16. a64 a64~ a16~ a4~ a8~ a32. a16~ a64 
a2.~ a8~ a32. a16~ a64 
a8~ a32. a64~ a16~ a8~ a32. a64~ a16~ a8~ a32. a4~ a16~ a64 
a8~ a32. a64~ a16~ a32. a8 a64~ a16~ a8~ a32. a4~ a16~ a64 
a4~ a8~ a32. a64~ a16~ a32. a4~ a8.~ a64 
a2~ a32. a64~ a8.~ a32. a8.~ a64 

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
