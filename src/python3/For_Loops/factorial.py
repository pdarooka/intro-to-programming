# For Loops: Factorial
import math

# Welcome message
print("Welcome!")

# Gets user input
num = int(input("Enter the number you want to find the factorial of: "))

# Prints the results
print(f"{num}! =", end=" ")

for i in range(1, num):
    print(str(i), end=" * ")
print(str(num))

print(f"\nUsing math library: {num}! = " + str(math.factorial(num)))

# Algorithm for factorial
temp = int(1)
for i in range(1, num+1):
    temp *= i

print(f"Using algorithm: {num}! = " + str(temp), end="\n\n")
