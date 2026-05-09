# Day 4: elif - Multiple choices
print("=== KCSE Grade Calculator ===")

score = int(input("Enter your score 0-100: "))

if score >= 80:
    grade = "A"
    comment = "Excellent! University ready."
elif score >= 70:
    grade = "B"
    comment = "Very Good! Keep it up."
elif score >= 60:
    grade = "C"
    comment = "Good. You passed."
elif score >= 50:
    grade = "D"
    comment = "Passed. Push harder."
else:
    grade = "E"
    comment = "Failed. Retake needed."

print(f"Score: {score}")
print(f"Grade: {grade}")
print(f"Comment: {comment}")
balance = 5000
withdraw = int(input("How much to withdraw? "))

balance = 5000
withdraw = int(input("How much to withdraw? "))

balance = 5000
withdraw = int(input("How much to withdraw? "))

balance = 5000
withdraw = int(input("How much to withdraw? "))

if withdraw > balance:
    print("Insufficient funds!")
elif withdraw <= 0:
    print("Invalid amount!")
else:
    balance = balance - withdraw
    print(f"Success! New balance: {balance}")