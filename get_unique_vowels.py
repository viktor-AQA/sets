def get_unique_vowels(s):
    vowels = "aeiouyAEIOUY"
    final_list = []
    for i in s:
        if (i in vowels) and i not in final_list:
            final_list.append(i)
        else:
            continue
    lst = set(final_list)
    print(lst)


get_unique_vowels("Hello World")