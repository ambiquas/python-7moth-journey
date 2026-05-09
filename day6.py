# Day 6: Lists - Store multiple values
print("=== Student Scores Tracker ===")

# A list holds multiple values in [ ]
scores = [85, 73, 46, 92, 67]

print(f"All scores: {scores}")
print(f"First student scored: {scores[0]}") # Lists start at 0
print(f"Number of students: {len(scores)}")
print(f"Highest score: {max(scores)}")
print(f"Average score: {sum(scores) / len(scores)}")

# Add a new score
scores.append(88)
print(f"After adding new student: {scores}")

# Loop through all scores
print("\nAll grades:")
for score in scores:
    if score >= 80:
        print(f"{score} = Grade A")
    elif score >= 70:
        print(f"{score} = Grade B")
    else:
        print(f"{score} = Grade C or below")