def my_long_word(n, s):
    words = s.split(' ')
    result = ''
    for word in words:
        length = 0
        for char in word:
            length += 1
        if length > n:
            result += word + ' '
    return result.strip()

s = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
print(my_long_word(3, s))
