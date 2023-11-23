def sum_of_even_numbers(L):
    sum = 0
    for num in L:
        if num % 2 == 0:
            sum += num
    return sum

L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
print(sum_of_even_numbers(L))
