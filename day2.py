# Day 2: Variables and Input
name = input("What's your name? ")
year_born = int(input("What year were you born? "))

age = 2026 - year_born

print(f"Hey {name}, you are {age} years old in 2026!")
print(f"In 5 years you'll be {age + 5}")