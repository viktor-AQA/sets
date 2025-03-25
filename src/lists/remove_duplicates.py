def remove_duplicates(lst):
    final_list = []
    for i in lst:
        if i in lst and i not in final_list:
            final_list.append(i)
        else:
            continue
    return final_list

final_list = remove_duplicates([1, 2, 2, 3, 4, 4])  # [1, 2, 3, 4]
print(remove_duplicates([1, 2, 2, 3, 4, 4]))

