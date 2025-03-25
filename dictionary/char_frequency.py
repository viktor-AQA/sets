def char_frequency(s):
    unique_s = set(s)
    frequency_dict = {char: s.count(char) for char in unique_s}

    return frequency_dict

print(char_frequency("hello"))
