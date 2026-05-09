# Day 7: Functions - Reusable code blocks

# 1. Define a function with 'def'
def get_grade(score):
    """This function converts a score to a letter grade"""
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "E"

# 2. Use the function multiple times
print("=== Grade Report ===")

students = [95, 68, 72, 49, 83, 77]

for i, score in enumerate(students, start=1):
    grade = get_grade(score)  # Call the function
    print(f"Student {i}: {score} = Grade {grade}")

# 3. Functions can be used anywhere
my_score = int(input("\nEnter YOUR score: "))
my_grade = get_grade(my_score)
print(f"You got Grade {my_grade}")