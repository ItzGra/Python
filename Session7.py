def get_average(marks):
    average = round(sum(marks) / len(marks), 2)
    return average
def get_grade(average):
    if average >= 16: return "Excellent"
    elif average >= 14: return "Very Good"
    elif average >= 10: return "Passed"
    else: return "Failed"
students = {
    "Mehdi": [16, 15, 12],
    "Mandi": [10, 13, 4],
    "Lola": [12, 8, 16]
}
for name, marks in students.items():
    print(f"{name}'s average: {get_average(marks)}")
passed_students = [name for name, marks in students.items() if get_average(marks) >= 10]
print(f"Passed: {passed_students}")
top_student = max(students, key=lambda name: get_average(students[name]))
print(f"Top student: {top_student} - {get_average(students[top_student])}/20")
unique_grades = {get_grade(get_average(marks)) for name, marks in students.items()}
print(f"Grades in class: {unique_grades}")