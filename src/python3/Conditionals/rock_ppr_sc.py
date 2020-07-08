# Conditionals: Rock, Paper and Scissors
import random

# Welcome message
print("Welcome!")

# Gets user input
rounds = int(input("How many rounds of Rock, Paper and Scissors do you want to play?\n"))

# Initializing variables
moves = ['rock', 'paper', 'scissor']

pl_score = 0
cpu_score = 0

for i in range(rounds):
    print(f"\nRound {i+1}")
    print(f"Player: {pl_score}\t\tCPU: {cpu_score}")
    
    usr_move = input("Please enter your next move (rock, paper or scissor): ").lower()
    cpu_move = random.randint(0, 2)
    
    print(f"\tComputer: {moves[cpu_move]}")
    print(f"\tUser: {usr_move}")

    if usr_move == moves[cpu_move]:
        print("It's a tie. Next round.")
        cpu_score += 1
        pl_score += 1
    elif usr_move == 'rock' and cpu_move == 2:
        print("Rock crushes scissors -- the user wins.")
        pl_score += 1
    elif usr_move == 'rock' and cpu_move == 1:
        print("Paper holds rocks -- the CPU wins.")
        cpu_score += 1
    elif usr_move == 'scissor' and cpu_move == 1:
        print("Scissors cut paper -- the user wins.")
        pl_score += 1
    elif usr_move == 'scissor' and cpu_move == 0:
        print("Rock crushes scissors -- the CPU wins.")
        cpu_score += 1
    elif usr_move == 'paper' and cpu_move == 0:
        print("Paper holds rocks -- the user wins.")
        pl_score += 1
    elif usr_move == 'paper' and cpu_move == 2:
        print("Scissors cut paper -- the CPU wins.")
        cpu_score += 1
    else:
        print("Invalid input -- the CPU wins")
        cpu_score += 1

print("\nFinal Game Results:")
print(f"\t\tRounds played: {rounds}")
print(f"\t\tRounds won by CPU: {cpu_score}")
print(f"\t\tRounds won by User: {pl_score}")

if cpu_score > pl_score:
    print("CPU WINS! Better Luck Next Time.")
elif cpu_score < pl_score:
    print("YOU WIN!")
else:
    print("It's a tie. GGWP")
