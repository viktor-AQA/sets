def merge_dicts(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1:
            dict1[key] += value
        else:
            dict1[key] = value
    return dict1

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dicts(dict1, dict2)) # {"a": 1, "b": 5, "c": 4}