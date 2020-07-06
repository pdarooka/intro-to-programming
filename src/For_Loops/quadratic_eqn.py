# For Loops: Quadratic Equation Solver
import cmath

# Welcome message
print("Welcome!")
print("A quadratic equation is always in the form ax^2 + bx + c = 0")
print("Your solutions can be complex or real numbers")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.")

num_queries = int(input("How many equations would you like to solve? "))

for i in range(num_queries):
    print(f"Solving equation #{i+1}")
    a = float(input("Please enter your value of a (coefficient of x^2): "))
    b = float(input("Please enter your value of b (coefficient of x): "))
    c = float(input("Please enter your value of c: "))

    print(f"\nThe equation formed is {a}x^2 + {b}x + {c} = 0")

    print(
        f"\nThe first solution to your equation is {((-1*b) + cmath.sqrt(b**2 - (4*a*c)))/2*a}")
    print(
        f"The second solution to your equation is {((-1*b) - cmath.sqrt(b**2 - (4*a*c)))/2*a}")

print("Thank you!")
