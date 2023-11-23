def round_number(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

def sort_list(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

numbers = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
rounded_numbers = [round_number(n) for n in numbers]
sorted_numbers = sort_list(rounded_numbers)
print(sorted_numbers)
