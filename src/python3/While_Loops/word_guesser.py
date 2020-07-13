# While Loops: Word Guesser Game
import random

# Welcome message
print("Welcome!")

# Initializing variables
game_dict = {
    "sports": ["basketball", "tennis", "football", "soccer"],
    "colors": ["red", "blue", "green", "yellow"],
    "fruits": ["apple", "orange", "mango", "tomato"],
    "animals": ["cat", "dog", "elephant", "mouse"]
}

game_keys = []
for key in game_dict.keys():
    game_keys.append(key)

flag = True
while flag:
    game_category = game_keys[random.randint(0, len(game_keys))]
    game_word = game_dict[game_category][random.randint(0, len(game_dict[game_category])]
    blank_word=[]
    for letter in game_word:
        blank_word.append('-')

    print(
        f"Word Category: {game_category}\t\t# of Letters = {len(blank_word)}")

    guess=''
    guess_count=0

    while guess != game_word:
        print(f"Current: {blank_word.join()}")
        guess_count += 1
        guess=input("Enter your guess: ")

        if guess == game_word:
            print(
                f"You have won this round. It took {guess_count} to guess the word.")
            break
        else:
