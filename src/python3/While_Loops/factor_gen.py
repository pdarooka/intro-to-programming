# While Loops: Factor Generator

# Welcome message
print("Welcome!")

# Generating Flags
flag = True

while flag:
    num = int(input("Enter a number: "))

    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)

    print("The factors of " + str(num) + " are:")
    for i in factors:
        print(i)

    print("\nIn summary:")
    for i in range(int(len(factors)/2)):
        print(f"{factors[i]} * {factors[-i-1]} = {num}")

    choice = input(
        "Would you like to continue the program? (y/n)\n").lower().strip()
    if choice == 'n':
        flag = False
        print("Thank you! Goodbye!")
