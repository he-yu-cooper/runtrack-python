def draw_triangle(height):

    for i in range(height):
        print(' ' * (height - i - 1) + '/' + ' ' * (2 * i) + '\\')


    print('-' * (2 * height))


draw_triangle(5)
