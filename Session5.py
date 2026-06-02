def get_mark_60_40(subject):
    exam = float(input(f"  {subject} exam mark: "))
    test = float(input(f"  {subject} test mark: "))
    return round(exam * 0.6 + test * 0.4, 2)

def get_test_only(subject):
    return float(input(f"  {subject} test mark: "))

def get_exam_only(subject):
    return float(input(f"  {subject} exam mark: "))

def get_grade(average):
    if average >= 16:
        return "Excellent"
    elif average >= 14:
        return "Very Good"
    elif average >= 10:
        return "Pass"
    else:
        return "Fail"

def process_student():
    name = input("Student name: ")
    print("\nEnter marks:")

    # coef 3
    writing   = get_mark_60_40("Academic Writing")

    # coef 2
    tls       = get_mark_60_40("TLS")
    ltal      = get_mark_60_40("LTAL")
    assessing = get_mark_60_40("Assessing English")
    comp_prog = get_test_only("Computer Programming")
    res_meth  = get_test_only("Research Methods")

    # coef 1
    textbooks  = get_exam_only("Textbooks Description")
    discourse  = get_exam_only("Discourse Analysis")
    ed_psych   = get_exam_only("Educational Psychology")

    # weighted sum
    weighted_sum = (
        writing   * 3 +
        tls       * 2 +
        ltal      * 2 +
        assessing * 2 +
        comp_prog * 2 +
        res_meth  * 2 +
        textbooks * 2 +
        discourse * 1 +
        ed_psych  * 1
    )

    total_coef = 3 + 2 + 2 + 2 + 2 + 2 + 2 + 1 + 1  # = 17
    final_average = round(weighted_sum / total_coef, 2)
    grade = get_grade(final_average)

    print(f"\n--- Results for {name} ---")
    print(f"  Academic Writing:       {writing}/20")
    print(f"  TLS:                    {tls}/20")
    print(f"  LTAL:                   {ltal}/20")
    print(f"  Assessing English:      {assessing}/20")
    print(f"  Computer Programming:   {comp_prog}/20")
    print(f"  Research Methods:       {res_meth}/20")
    print(f"  Textbooks Description:  {textbooks}/20")
    print(f"  Discourse Analysis:     {discourse}/20")
    print(f"  Educational Psychology: {ed_psych}/20")
    print(f"\n  Final Average: {final_average}/20 — {grade}")
    return final_average >= 10
num_students = int(input("Enter number of students: "))
passed_count = 0
for i in range(1, num_students + 1):
    print(f"\n--- Student {i} ---")
    if process_student():
        passed_count += 1

print(f"\nTotal passed: {passed_count}/{num_students}")