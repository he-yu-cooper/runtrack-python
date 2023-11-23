def find_max_min(L):
    max_value = max(L)
    min_value = min(L)
    return max_value, min_value

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
max_value, min_value = find_max_min(L)
print("maximum:", max_value)
print("minimun:", min_value)
