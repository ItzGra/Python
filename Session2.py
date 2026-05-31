name = input('What is your name? ')
mark1 = float(input("What is your mark in English? "))
mark2 = float(input("What is your mark in French? "))
mark3 = float(input("What is your mark in Philosophy? "))

average = round((mark1 + mark2 + mark3) / 3, 2)

if average >= 16:
    grade = "Excellent"
elif average >= 14:
    grade = "Very Good"
elif average >= 10:
    grade = "Pass"
else:
    grade = "Fail"

print(f"\nStudent Name: {name}")
print(f"Average: {average}")
print(f"Result: {grade}")