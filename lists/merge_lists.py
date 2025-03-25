def merge_lists(list1, list2):
    list3 = list1 + list2
    list_final = list()

    for i in list3:
        if i not in list_final:
            list_final.append(i)
        else:
            continue
    return list_final

list_final = merge_lists([1, 2, 3], [3, 4, 5])
print(merge_lists([1, 2, 3], [3, 4, 5]))  # [1, 2, 3, 4, 5]
