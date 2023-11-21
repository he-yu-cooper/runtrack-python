s = "abcdefghijklmnopqrstuvwxyz" * 10
index = 0
for i in range(1, 101):
    if i % 2 != 0:
        print(s[index:index+i].center(100))
        index += i
