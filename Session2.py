name = input('What is your name? ')
mark1 = float(input("What is your mark in English? "))
mark2 = float(input("What is your mark in French? "))
mark3 = float(input("What is your mark in Philosophy? "))

average = round((mark1 + mark2 + mark3) / 3, 2)
passed = average >= 10
print(f"Hello {name}! Your average in English, French, and Philosophy is {average}.")
print(f"Passed: {'Yes' if passed else 'No'}")