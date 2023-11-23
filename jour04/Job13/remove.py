def remove_duplicates(L):
    new_list = []
    for i in L:
        if i not in new_list:
            new_list.append(i)
    return new_list

L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print(remove_duplicates(L))


