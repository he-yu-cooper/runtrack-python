try:
    a = float(input("Enter length a: "))
    b = float(input("Enter length b: "))
    c = float(input("Enter length c: "))
except ValueError:
    print("Please enter valid numerical values.")
    exit()
sides = [a, b, c]
sides.sort()

if sides[0] + sides[1] > sides[2]:
    # Determine the type of triangle
    if sides[0] == sides[1] == sides[2]:
        print("The triangle is equilateral.")
    elif sides[0] == sides[1] or sides[1] == sides[2]:
        print("The triangle is isosceles.")
    elif sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("The triangle is right-angled.")
    else:
        print("The triangle is scalene.")
else:
    print("The lengths do not form a triangle.")
