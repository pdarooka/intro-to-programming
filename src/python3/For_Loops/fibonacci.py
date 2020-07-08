# For Loops: Fibonacci

# Welcome message
print("Welcome!")

# Gets user input
num_queries = int(
    input("How many digits of the fibonacci sequence would you like to see?\n"))

# Processes the sequence
fib = [1, 1]
for i in range(2, num_queries):
    fib.append(fib[i-1]+fib[i-2])

print(f"The sequence is as follows: {fib}")

# Computing ratios
ratios = []
for i in range(len(fib)-1):
    ratios.append(fib[i+1]/fib[i])

# TODO: Prints 'None' in the end (Issue)
print(print(
    f"The ratio of the sequence is: {ratios[len(ratios) - 1]}\nThis is the same as the Golden Ratio"))
