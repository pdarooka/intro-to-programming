# Dictionaries: Yes/No Polling

# Welcome message
print("Welcome!")

# Gets user input
issue = input("What is the issue you want to start a poll on?\n")
num_voters = int(input("How many voters will be taking the poll?\n"))
pwd = input("\tCreate password: ")

# Initializing variables
yes_ = 0
no_ = 0
results = {}

for i in range(num_voters):
    usr_name = input("\tEnter Your Name: ").title()
    if usr_name not in results.keys():
        print(issue)
        vote = input("Please enter your decision: ").lower()[0]

        if vote == 'y':
            yes_ += 1
        elif vote == 'n':
            no_ += 1
        else:
            print("Invalid input. Your vote will not influence the poll's results.")

        results[usr_name] = vote
        print("Thank you for voting.")
    else:
        print("You have already voted.")

# Prints summary
print('\nResults of the poll:\n')
print(f"These people have voted in the poll:\n{results.keys()}")
print(f"On the following issue: {issue}")

if yes_ > no_:
    print(f"Yes wins! {yes_} to {no_}")
else:
    print(f"No wins! {no_} to {yes_}")

# Admin login
if input("To see the voting results enter the password: ") == pwd:
    for k, v in results.items():
        print(f"Voter: {k}\t\tVote (y/n)): {v}")
else:
    print("That is not the correct password!")
