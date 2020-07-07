# Conditionals: Voter Registration

# Welcome message
print("Welcome!")

# Gets user input
name = input("What is your name? ").title()
age = int(input("What is your age? "))

parties = ['Republican', 'Democratic', 'Independent', 'Green']

# Conditionals and Output
if age < 18:
    print("You are not old enough to register to vote.")
else:
    print(f"\nThe parties you can vote for are {parties}\n")
    desired = input("What party would you like to join? ").title()
    print(f"Congratulations, {name}! You have joined the {desired} party.")

    if desired == "Republican" or desired == "Democratic":
        print("It is a major party!")
    elif desired == "Independent":
        print("You are an independent person!")
    else:
        print("That is not a given party!")
    