# Basic Data Types: Letter Counter

# Welcome message
print("Welcome!")

# Gets user's name
name = input("Please enter your full name: ")

# Greetings + Features message
print("\nHello, " + name)
print("I will count the number of times that a specific letter occurs in a message.")

# Gets user's inputs
message = input("Please enter some text: ").upper()
letter = input(
    "Which letter would you like to count the occurrences of: ")

# Processes and Outputs Letter Count
letter_count = message.count(letter.upper())
print(f"{name}, the input message has {letter_count} {letter}'s in it.")
