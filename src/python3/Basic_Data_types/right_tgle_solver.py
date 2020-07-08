import math

# Basic Data Types: Right-Angle Triangle Solver

# Welcome message
print("Welcome!")

# Gets user's inputs
leg1 = float(
    input("Please enter the length of the first leg of the triangle: "))
leg2 = float(
    input("Please enter the length of the second leg of the triangle: "))

# Calculating hypotenuse
hypo = float(math.sqrt((leg1 ** 2) + (leg2 ** 2)))
area = float(0.5 * leg1 * leg2)

# Outputs hypotenuse length and area of the right-angle triangle
print(
    f"\nThe length of the hypotenuse of the right-angle triangle is {round(hypo, 4)}\t")
print(f"The area of the right-angle triangle is {round(area, 4)}\t")
