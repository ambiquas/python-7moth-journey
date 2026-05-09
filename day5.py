# Day 5: Loops - Grade multiple students
print("=== Grade 3 Students ===")

for student in range(1, 4):
    print(f"\n--- Student {student} ---")
    score = int(input("Enter score: "))
    
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "E"
    
    print(f"Student {student} got Grade {grade}")

print("\nAll students graded!")