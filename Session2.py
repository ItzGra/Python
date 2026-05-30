name = input(f'What is your name? ')
mark1 = float(input(f"What is your mark in English? "))
mark2 = float(input(f"What is your mark in French? "))
mark3 = float(input(f"What is your mark in Philosophy? "))

average = (mark1 + mark2 + mark3) / 3
passed = average >= 10
print(f"Hello {name}! Your average in English, French, and Philosophy is {average}.")
print(f"Passed: {passed}")