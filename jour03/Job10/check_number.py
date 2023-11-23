def check_number(num):
    if isinstance(num, (int, float)) and num > 0:
        if int(num) == num:
            if int(num) % 2 == 0:
                print(f"{num} is an even number")
            else:
                print(f"{num} is an odd number")
        else:
            print("The input is not an integer")
    else:
        print("The input is not a positive number")

check_number(11)
check_number(10)
check_number(-1)
check_number(0)
check_number(3.5)