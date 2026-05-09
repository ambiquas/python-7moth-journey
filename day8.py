# Day 8: Dictionaries - Key:Value pairs
students = {
    "Benson": 95,
    "Alice": 68,
    "John": 72,
    "Mary": 49
}

# Get Benson's score
print(f"Benson scored: {students['Benson']}")

# Add new student
students["Peter"] = 83

# Loop through all
for name, score in students.items():
    print(f"{name} = {score}")