def fruits_list():
    fruits = ["apple", "cherry", "orange"]
    fruits.append("melon")
    fruits[fruits.index("orange")] = "mango"
    return fruits
print(fruits_list())


