def draw_carpet_with_diagonal_and_frame(n):
    
    print("+" + "-" * (2 * n + 1) + "+")

    for i in range(n + 1):

        print("|", end="")
        
        for j in range(n + 1):
            if i == n - j:
    
                print(' ', end=' ')
            else:
                print('#', end=' ')
        
        print("|")
    print("+" + "-" * (2 * n + 1) + "+")
draw_carpet_with_diagonal_and_frame(10)
