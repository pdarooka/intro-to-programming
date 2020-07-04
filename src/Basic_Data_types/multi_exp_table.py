# Basic Data Types: MPH to KmPH converter

# Welcome message
print("Welcome!")

# Gets user's inputs
name = input("Please enter you name: ").title().strip()
number = float(input("Please enter a number: "))

tmp = name + ", Math is cool!"

# Printing the multiplication table
print(f"Multiplication Table For {number}")

print(f"{number} x 1 = {round(number * 1, 3)}")
print(f"{number} x 2 = {round(number * 2, 3)}")
print(f"{number} x 3 = {round(number * 3, 3)}")
print(f"{number} x 4 = {round(number * 4, 3)}")
print(f"{number} x 5 = {round(number * 5, 3)}")
print(f"{number} x 6 = {round(number * 6, 3)}")
print(f"{number} x 7 = {round(number * 7, 3)}")
print(f"{number} x 8 = {round(number * 8, 3)}")
print(f"{number} x 9 = {round(number * 9, 3)}")

# Printing the exponent table
print(f"Exponent Table For {number}")

print(f"{number} ^ 1 = {round(number ** 1, 3)}")
print(f"{number} ^ 2 = {round(number ** 2, 3)}")
print(f"{number} ^ 3 = {round(number ** 3, 3)}")
print(f"{number} ^ 4 = {round(number ** 4, 3)}")
print(f"{number} ^ 5 = {round(number ** 5, 3)}")
print(f"{number} ^ 6 = {round(number ** 6, 3)}")
print(f"{number} ^ 7 = {round(number ** 7, 3)}")
print(f"{number} ^ 8 = {round(number ** 8, 3)}")
print(f"{number} ^ 9 = {round(number ** 9, 3)}")

# Printing the message
print("\n" + tmp)
print("\t" + tmp.lower())
print("\t\t" + tmp.title())
print("\t\t\t" + tmp.upper())
