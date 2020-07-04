# Lists: Grade Sorter

# Welcome message
print("Welcome!")

#Gets user input
grades = []

grades.append(int(input("Enter your grade: ")))
grades.append(int(input("Enter your grade: ")))
grades.append(int(input("Enter your grade: ")))
grades.append(int(input("Enter your grade: ")))
grades.append(int(input("Enter your grade: ")))

print(f"Your grades are {grades}")

# Prints the sorted list
grades.sort(reverse = True)
print(f"Your grades from highest to lowest are {grades}")

# Drops lowest grades
print("The lowest two grades will now be dropped.")
print(f"Removed grade: {grades.pop()}")
print(f"Removed grade: {grades.pop()}")

# Prints remaining grades
print(f"Your remaining grades are {grades}")
print(f"Good Job! Your highest grade is a {grades[0]}")
