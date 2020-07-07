# Conditionals: Coin Toss
import random

# Welcome message
print("Welcome!")

# Gets user input
times = int(input("How many times would you like to flip the coin? "))

to_see = input("Would you like to see the result of each individual coin flip or not? (y/n) ")
if to_see.lower() == 'y':
    to_see = True
else:
    to_see = False

# Flips the coin
num_heads = 0
num_tails = 0

for counter in range(times):
    x = int(random.randint(0,1))
    if x == 0:
        num_heads += 1
        if to_see:
            print("HEADS")
    else:
        num_tails += 1
        if to_see:
            print("TAILS")
    if num_heads == num_tails:
        print(f"At {counter} flips, the number of heads and tails were equal at {num_heads} each.")

# Processes the percentages
heads_pctg = 100 * num_heads / times
tails_pctg = 100 * num_tails / times

# Prints the results
print(f"\nResults of flipping the coin {times} times:")
print("Side\t\tCount\t\tPercentage")
print(f"Heads\t\t{num_heads}/{times}\t\t{round(heads_pctg,2)}%")
print(f"Tails\t\t{num_tails}/{times}\t\t{round(tails_pctg,2)}%")