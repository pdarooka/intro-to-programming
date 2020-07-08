# Conditionals: Number Guesser
import random

# Welcome message
print("Welcome!")

# Gets user input
name = input("What is your name?\n")

# Instructions
guess = int(input("I am thinking of a number between 1 and 10. Can you guess it?\n"))
num = random.randint(1, 10)
counter = 0

correct = False

for i in range(5):
    if guess == num:
        counter += 1
        print(f"\nGood job, {name}! You guessed my number in {counter} guesses.")
        correct = True
        break
    elif guess > num:
        counter += 1
        guess = int(input(f"Your guess is too high.\nTake a guess: "))
    else:
        counter += 1
        guess = int(input(f"Your guess is too low.\nTake a guess: "))

if not correct:
    print(f"\nGame over. The number I was thinking of was {num}")