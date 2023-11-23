def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    elif operator == '%':
        return num1 % num2
    else:
        return "Error: Invalid operator"

    

print(calcule(1, '+', 2))  
print(calcule(3, '-', 4)) 
print(calcule(5, '*', 6))  
print(calcule(0, '/', 0))  
print(calcule(100, '%', 5))  


