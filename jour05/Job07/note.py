def round_grades(grades):
    rounded_grades = []
    for grade in grades:
        if grade >= 38:
            remainder = grade % 5
            if remainder >= 3:
                grade += (5 - remainder)
        rounded_grades.append(grade)
    return rounded_grades
import random

def generate_scores(num_students):
    return [random.randint(0, 100) for _ in range(num_students)]
scores = generate_scores(10)

print(scores)
rounded_scores = round_grades(scores)
print(rounded_scores)