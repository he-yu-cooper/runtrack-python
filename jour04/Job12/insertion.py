def insertion_sort(lst):

    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        
  
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        
    
        lst[j + 1] = key


my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)

print( my_list)
