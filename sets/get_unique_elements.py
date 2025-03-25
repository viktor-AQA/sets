def get_unique_elements(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
        else:
            continue
    print(new_lst)


get_unique_elements([1, 2, 2, 3, 4, 4, 4, 5])