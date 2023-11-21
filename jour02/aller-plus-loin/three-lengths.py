a = float(input("Please enter length a: "))
b = float(input("Please enter length b: "))
c = float(input("Please enter length c: "))
if a + b > c and a + c > b and b + c > a:
    print("A triangle can be constructed.")
    
    if a == b == c:
        print("This is an equilateral triangle.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        if a == b or a == c or b == c:
            print("This is an isosceles right-angled triangle.")
        else:
            print("This is a right-angled triangle.")
    elif a == b or a == c or b == c:
        print("This is an isosceles triangle.")
    else:
        print("This is a scalene triangle.")
else:
    print("A triangle cannot be constructed.")
