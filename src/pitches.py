

PITCHES = ["A", "B", "C", "D", "E", "F", "G"]

SHARP_OCTAVE = ["C", "C♯", "D", "D♯", "E", "F", "F♯", "G", "G♯", "A", "A♯", "B"]
FLAT_OCTAVE = ["C", "D♭", "D", "E♭", "E", "F", "G♭", "G", "A♭", "A", "B♭", "B"]


# use index to get spn values
def index_to_spn(mode, index):
    index += 9  # fills 0 octave
    octave = int(index / 12)
    if mode == "♭":
        pitch = FLAT_OCTAVE[index % 12]
    else:
        pitch = SHARP_OCTAVE[index % 12]
    return f"{pitch}{octave}"


#  size 88 lists of either sharp or flat named spn strings
SHARP_SPN_LIST = [index_to_spn("♯", index) for index in range(88)]
FLAT_SPN_LIST = [index_to_spn("♭", index) for index in range(88)]


def choose_spn_list(pitch, scale):
    if scale == "major":
        if pitch in ["G", "D", "A", "E", "B"] or "♯" in pitch:
            return SHARP_SPN_LIST
        else:
            return FLAT_SPN_LIST
    elif "minor" in scale:
        if pitch in ["B", "E"] or "♯" in pitch:
            return SHARP_SPN_LIST


if __name__ == "__main__":
    print(SHARP_SPN_LIST)