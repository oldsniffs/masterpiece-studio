# MasterpieceSymphonies

This program procedurally generates piano music within certain user-defined parameters, and outputs sheet music in .pdf format using the GNU-licensed engraving program, Lilypond.
Requires at least Python 3.8 and Lilypond installed, with Lilypond added to PATH variable for automatic output.

Run studio.py

The "Structure" section allows segmenting the composition into different styles. Each segment of the structure has an attached style, defining its musical qualities. This can be edited in the "Style" section. A "configuration" can be saved or loaded which holds the full Style and Structure settings. The "Compose" section allows you to generate a new composition with the actively loaded configuration.

Output is saved to the compositions folder
