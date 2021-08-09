# Default configuration

DEFAULT_LENGTH = 14


# Weights
WEIGHTS_STANDARD = {
    'whole_prime': 6,
    'dwhole_prime': 1,
    'half_prime': 16,
    'dhalf_prime': 5,
    'quarter_prime': 26,
    'dquarter_prime': 3,
    'eighth_prime': 20,
    'deighth_prime': 3,
    'sixteenth_prime': 6,
    'dsixteenth_prime': 2,
    'thirtysecond_prime': 2,
    'dthirtysecond_prime': 0,
    'sixtyfourth_prime': 1,
    'dsixtyfourth_prime': 0,
    'whole_pair': 0,
    'dwhole_pair': 0,
    'half_pair': 0,
    'dhalf_pair': 0,
    'quarter_pair': 0,
    'dquarter_pair': 0,
    'eighth_pair': 2,
    'deighth_pair': 0,
    'sixteenth_pair': 4,
    'dsixteenth_pair': 0,
    'thirtysecond_pair': 9,
    'dthirtysecond_pair': 0,
    'sixtyfourth_pair': 0,
    'dsixtyfourth_pair': 9,
    'eighth_length': [8, 3, 2, 1, 1, 0, 0],
    'sixteenth_length': [2, 8, 4, 2, 1, 1, 0],
    'thirtysecond_length': [4, 12, 8, 4, 4, 1, 1],
    'sixtyfourth_length': [4, 12, 8, 4, 4, 1, 1],
    'deighth_length': [8, 3, 2, 1, 1, 0, 0],
    'dsixteenth_length': [2, 8, 4, 2, 1, 1, 0],
    'dthirtysecond_length': [4, 12, 8, 4, 4, 1, 1],
    'dsixtyfourth_length': [4, 12, 8, 4, 4, 1, 1],
}

# Bounds
BOUNDS_STANDARD = {
    'left_lower': 10,
    'left_upper': 40,
    'right_lower': 30,
    'right_upper': 60,
}

# Anchors
ANCHORS_STANDARD = {
    'primary_gravity': 16,
    'primary_velocity': 14,
    'secondary_gravity': 8,
    'secondary_velocity': 14,
    'secondary_spawn': 10,
    'secondary_longevity': 8,  # in measures?
    'tertiary_gravity': 28,
    'tertiary_velocity': 0,
    'tertiary_spawn': 10,
    'tertiary_longevity': 4,
}

# Style
STANDARD_STYLE = {
    'name': 'Standard',
    'timesig_num': 4,
    'timesig_den': 4,
    'bpm': 60,
    'keysig_atonal': False,
    'keysig_acc':  "",
    'keysig_pitch': "C",
    'keysig_scale': "Major",
    'ranges_mode': "♯",
    'bounds': BOUNDS_STANDARD,
    'weights': WEIGHTS_STANDARD,
    'snap': 50,
    'rest': 10,
    'division_beats': [2],
    # number of division_beats      ---> duple, triple quadruple
    # how beats are divided         ---> simple = by 2, complex
    'meter': [2], # list of meters matching division_beats -- 2 means simple, 3 means triple
    'meter_unit': [], # index of meter unit. determined by meter and time den (regular beat divided by meter)
    'meter_strength': 70,
    'anchors': ANCHORS_STANDARD,
}
