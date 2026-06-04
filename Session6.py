bob_marks = [6.75, 15, 12, 17, 9]
bob_marks.sort(reverse=True)
average = round(sum(bob_marks) / len(bob_marks), 2)
print(f"Highest: {bob_marks[0]}")
print(f"Lowest: {bob_marks[-1]}")
print(f"Average: {average}")
passing = [m for m in bob_marks if m >= 10]
print(f"Passing marks: {passing}")
top3 = bob_marks[:3]
print(f"Top 3: {top3}")
modules = ("English", "Math", "Biology", "Religion", "Philosophy")
for module in modules:
    print(module)
    