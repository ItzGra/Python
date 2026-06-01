num_students = int(input("Enter the number of students: "))
passed_count = 0
for i in range(1, num_students + 1):
    print(f"\n--- Student {i} ---")
    name = input("Name: ")
    mark = float(input("Mark: "))
    while mark < 0 or mark > 20:
        print("Invalid mark. Please enter a mark between 0 and 20.")
        mark = float(input("Mark: "))
    if mark >= 16:
        grade = "Excellent"
    elif mark >= 14:
        grade = "Very Good"
    elif mark >= 10:
        grade = "Pass"
    else:
        grade = "Fail"
    if mark >= 10:
        passed_count += 1
    print(f"Mark: {mark}/20")
    print(f"Grade: {grade}")

print(f"\nTotal students passed: {passed_count} out of {num_students}")
