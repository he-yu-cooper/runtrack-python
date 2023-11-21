N = int(input("Please enter an integer greater than 0: "))

# Check if the input is valid
if N <= 0:
    print("Invalid input. Please enter an integer greater than 0.")
else:
    # Print the multiplication tables
    for i in range(1, N+1):
        for j in range(1, 11):
            print(f"{i} * {j} = {i*j}")
        print("-" * 20)