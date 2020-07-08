# Dictionaries: Thesaurus
import random

thesaurus = {
    'hot': ['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    'cold': ['chilly', 'cool', 'freezing', 'frigid', 'polar'],
    'happy': ['content', 'cheery', 'merry', 'jovial', 'jocular'],
    'sad': ['unhappy', 'downcast', 'miserable', 'glum', 'melancholy']
    }

# Welcome message
print("Welcome!")

# Prints the keys
print("Here are the words in the thesaurus:")
for k in thesaurus.keys():
    print(k)

# Gets user input
desired = input("What word would you like a synonym for: ").lower()
if desired in thesaurus.keys():
    print(f"A synonym for {desired.title()} is {thesaurus[desired][random.randint(0,4)]}.")
else:
    print("Could not find a synonym for the given word.")

if input("\nWould you like to see the whole thesaurus? (y/n)\n").lower() == 'y':
    for k, v in thesaurus.items():
        print(f"The synonyms for {k} are:")
        for word in thesaurus[k]:
            print(f"\t- {word.title()}")
else:
        print("No worries! Good bye.")
