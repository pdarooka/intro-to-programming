# For Loops: Factorial

# Welcome message
print("Welcome!")

# Gets user input
name = input("What is your name?\n").title()
num_queries = int(input("How many grades would you like to enter?\n"))

grades = []
for i in range(num_queries):
    grades.append(float(input("Enter your grade: ")))
grades.sort(reverse=True)

grades_avg = round(float(sum(grades)/num_queries), 2)

print(
    f"Hello, {name}!\n\tThe grade point average for your {num_queries} grades entered is {grades_avg}.\n\tHighest grade: {grades[0]}\n\tLowest grade: {grades[len(grades)-1]}")

desired_grade = round(
    float(input("\nWhat is your desired grade point average?\n")), 2)

required = round(desired_grade * (num_queries+1) - sum(grades), 2)

print(
    f"\nGood Luck, {name}! You need to score a {required} to get a grade point average of {desired_grade}.")

temp = grades.copy()

to_change = float(input("\nWhat grade value would you like to change?\n"))
temp.remove(to_change)

to_add = round(float(input("\nWhat grade value would you add instead?\n")), 2)
temp.append(to_add)

temp.sort(reverse=True)

upd_grades_avg = round(float(sum(temp)/num_queries), 2)

print(
    f"Hello, {name}!\n\tThe grade point average for your {num_queries} grades entered is {upd_grades_avg}.\n\tHighest grade: {temp[0]}\n\tLowest grade: {temp[len(temp)-1]}\n")

print(
    f"Your previous GPA was {grades_avg}, the updated GPA is {upd_grades_avg}.\nYour GPA has changed by {upd_grades_avg - grades_avg} points.\nYour original grades list is however unchanged: {grades}\n")
