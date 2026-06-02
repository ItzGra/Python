def writing_module(m1, t1):
    writing_average = round((m1 * 0.6 + t1 * 0.4), 2)
    return writing_average
def coef2_modules(t2, m3, t3, m4, t4, t5, m6, t6, m7):
    coef2_average = round((t2 + m3 * 0.6 + t3 * 0.4 + m4 * 0.6 + t4 * 0.4 + t5 + m6 * 0.6 + t6 * 0.4 + m7) / 6, 2)
    return coef2_average
def coef1_modules(m8, m9):
    coef1_average = round((m8 + m9) / 2, 2)
    return coef1_average

student_name = input("Enter the student's name: ")
m1, t1 = float(input("Writing exam mark: ")), float(input("Writing test mark: "))
t2 = float(input("Computer programming test mark: "))
m3, t3 = float(input("TLS exam mark: ")), float(input("TLS test mark: "))
m4, t4 = float(input("LTAL exam mark: ")), float(input("LTAL test mark: "))
t5 = float(input("Research methods test mark: "))
m6, t6 = float(input("Assessing English exam mark: ")), float(input("Assessing English test mark: "))
m7 = float(input("Textbooks description exam mark: "))
m8 = float(input("Discourse analysis exam mark: "))
m9 = float(input("Educational psychology exam mark: "))

marks = [m1, t1, t2, m3, t3, m4, t4, t5, m6, t6, m7, m8, m9]
if any(mark < 0 or mark > 20 for mark in marks):
    print("Invalid mark detected. Please ensure all marks are between 0 and 20.")
    exit()

writing_average = writing_module(m1, t1)
coef2_average = coef2_modules(t2, m3, t3, m4, t4, t5, m6, t6, m7)
coef1_average = coef1_modules(m8, m9)
print(f"\nWriting Module Average: {writing_average}")
print(f"Coefficient 2 Modules Average: {coef2_average}")
print(f"Coefficient 1 Modules Average: {coef1_average}")

final_average = round((writing_average * 3 + coef2_average * 2 + coef1_average) / 17, 2)

if final_average >= 16:
    final_grade = "Excellent"
elif final_average >= 14:
    final_grade = "Very Good"
elif final_average >= 10:
    final_grade = "Pass"
else:
    final_grade = "Fail"
print(f"\nStudent Name: {student_name}")
print(f"Final Average: {final_average}")
print(f"Final Grade: {final_grade}")