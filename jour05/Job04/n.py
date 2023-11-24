def draw_diagonal(n):
    # 打印图案的顶部边框
    print(' ' + '_' * (n+2) + ' ')

    # 打印图案的每一行
    for i in range(n+1):
        print('|' + '#' * i + ' ' * (n - i) + '#' * i + '|')

    # 打印图案的底部边框
    print('|' + '_' * (n+2) + '|')

# 调用函数
draw_diagonal(10)
