def group_by_first_letter(strings):
    grouped = {}
    for string in strings:
            first_letter = string[0]
            if first_letter not in grouped:
                grouped[first_letter] = []
            grouped[first_letter].append(string)
    return grouped

strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings))
