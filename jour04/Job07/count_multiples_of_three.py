def count_multiples_of_three(L):
    count = 0
    for num in L:
        if num % 3 == 0:
            count += 1
    return count

L = [8, 24, 48, 2, 16]
print(count_multiples_of_three(L))
