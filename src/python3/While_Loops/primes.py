# While Loops: Prime Numbers
import time

# Welcome message
print("Welcome!")

flag = True
while flag:
    print("Press 1: Determine if a specific number is prime.")
    print("Press 2: Determine all prime numbers within a set range.")
    choice = input("Enter your choice: ")

    if choice == '1':
        num = int(input("Enter the number: "))
        prime_status = True

        for i in range(2, num):
            if num % i == 0:
                prime_status = False
                break

        if prime_status:
            print(f"The number {num} is a prime number.")
        else:
            print(f"The number {num} is not a prime number.")

    elif choice == '2':
        low = int(input("Enter the lower bound: "))
        up = int(input("Enter the upper bound: "))
        start_time = time.time()
        primes = []

        for i in range(low, up):
            if i > 1:
                prime_status = True
            else:
                prime_status = False

            for p in range(2, i):
                if i % p == 0:
                    prime_status = False
                    break

            if prime_status:
                primes.append(i)

        end_time = time.time()

        delta_time = round(end_time - start_time, 4)
        print(f"The numbers {primes} are a prime number.")
        print(f"The calculation took {delta_time} seconds.")
    else:
        print("Invalid input.")

    continue_prog = input(
        "Would you like to continue this program? (y/n)\n").lower().strip()[0]
    if continue_prog == 'n':
        flag = False
        print("Good bye. Thank you!")
