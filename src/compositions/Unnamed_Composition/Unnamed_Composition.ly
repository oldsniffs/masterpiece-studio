upper = {
    \clef treble
    \key c \major
    \time 4/4

dis'4 g'8. b16 b8 f'8 f'8 a'8 
gis''8 gis''8 a16. cis''32~ cis''8~ cis''16. e''32~ e''8 a''4 
ais'16. g''32~ g''8 ais'4 d''16. c''32 fis8~ fis4 
c''4~ c''16. c'16. ais16~ ais16 a'8. fis'16 gis''8. 
dis''16 cis'8 b'16~ b'4.. fis'16~ fis'4 
c''8. e16 cis''16 f'8.~ f'2 
b'4~ b'16 fis'8 cis''16 f''16. a''32 g8~ g16. f'16. a'16 
a'8. gis'16 b16 f''8 fis''16 c''8. a''16~ a''4 
g16 f8 gis16 b2. 
f4 g'4 fis''8 b'16 f''16 fis'4 
b2 ais8. gis''16 gis'8. ais'16 
a'8. fis'16 fis'8. b'16 e''16 a'8 dis16 f''4 
dis''2~ dis''8. gis16 f4 
b'4 g''4 ais2 
b2 e'2 
}

lower = {
    \clef bass
    \key c \major
    \time 4/4

c8 ais,8 c'2. 
fis4 e,4 g4 dis4 
a,4 dis2 fis8 a,8 
gis,4. f,8~ f,8 cis8 dis4 
g,,2. gis,4 
a,,2. fis,4 
a4 c'2 gis,4 
g,,4 cis,2. 
f,4 fis,2. 
ais4 fis8 a8 c2 
e,8 a,,8~ a,,2 ais,8 a8 
c'4. e,8 cis8 gis,,8 cis8 dis8 
gis,4 cis'8 dis8 g,,8 ais,8~ ais,8 a8 
c,2.. a,,8 
e8 gis8 d,8 ais,,8 dis,4 b4 

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
