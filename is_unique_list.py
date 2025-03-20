def is_unique_list(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
        else:
            continue
    print(new_lst == lst)

is_unique_list([1, 2, 3, 4])