name = input('What is your name? ')
mark1 = float(input("What is your mark in English? "))
mark2 = float(input("What is your mark in French? "))
mark3 = float(input("What is your mark in Philosophy? "))

if mark1 < 0 or mark1 > 20 or mark2 < 0 or mark2 > 20 or mark3 < 0 or mark3 > 20:
    print("Error: Marks should be between 0 and 20.")
else:
    average = round((mark1 + mark2 + mark3) / 3, 2)
    if average >= 16:
        grade = "Excellent"
    elif average >= 14:
        grade = "Very Good"
    elif average >= 10:
        grade = "Pass"
    else:
        grade = "Fail"
    print(f"\nStudent: {name}")
    print(f"Average: {average}")
    print(f"Result: {grade}")