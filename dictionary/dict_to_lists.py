def dict_to_lists(my_dict):
    list_key = list()
    list_value = list()
    for key, value in my_dict.items():
        list_key.append(key)
        list_value.append(value)
    return list_key, list_value

my_dict = {"a": 1, "b": 2, "c": 3}
print(dict_to_lists(my_dict))  # (["a", "b", "c"], [1, 2, 3])

