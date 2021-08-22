from pitches import *
from custom_logging import *


SCALES = {
    "major":[2, 2, 1, 2, 2, 2, 1]*4,
    "minor":[2, 1, 2, 2, 1, 2, 2]*4
}

CHORDS = {
    "major": (4, 3),
    "minor": (3, 4),
    "dominant_seventh": (3, 4, 3),
}


# style needs to update its key map every time key is changed
# returns list of pitch indexes representing all pitches in the key
# Also, the falsebeing loop was probably better
def map_key(pitch, scale):
    log_debug(f"Making new keymap for key {pitch} {scale}")
    piano_keyboard = [i for i in range(88)]

    spn_list = choose_spn_list(pitch, scale)
    log_debug(f"Got spn list {spn_list}")
    start_index = spn_list.index(pitch+"1")
    scale_map = SCALES[scale]
    keymap = []

    step = 0
    index = start_index
    while index < 87:  # Mapping up
        try:
            keymap.append(index)
            index += scale_map[step]
            step += 1
            if step == len(scale_map):
                step = 0
        except IndexError as e:
            log_debug(f"Passed top of keyboard at {index}")

    scale_map = [i for i in reversed(scale_map)]
    step = -1
    index = start_index
    while index > 0:  # Mapping down
        try:
            keymap.insert(0, index)
            index -= scale_map[-step]
            step += 1
            if step == len(scale_map):
                step = 0
        except IndexError:
            log_debug(f"Passed bottom of keyboard at {index}")

    return keymap


if __name__ == "__main__":
    print(map_key("A♯", "major"))