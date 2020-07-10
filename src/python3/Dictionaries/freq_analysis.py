# Dictionaries: Frequency Analysis
from collections import Counter

# Welcome message
print("Welcome!")

non_letters = [
    '&', '%', '$', '!', ' ', ', ', '.', ' /',
    '(', ')', ';', '-', '\'', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
]

# First time
# Initializing variables
text = input("Enter the text:\n").lower().strip()

for i in non_letters:
    text = text.replace(i, '')

total_occurrences2 = len(text)
letter_count2 = Counter(text)

# Frequency Analysis Output
print("\nHere is a frequency analysis from the entered text:")
for k in sorted(letter_count2.keys()):
    print(
        f'{k} : {letter_count2[k]} = {round(100*letter_count2[k]/total_occurrences2,2)}%')

ordered_letter_count2 = letter_count2.most_common()

text_ordered_letters2 = []

for i in ordered_letter_count2:
    text_ordered_letters2.append(i[0])

print("Letters ordered from highest to lowest frequency:")
for i in text_ordered_letters2:
    print(i, end='')
print()

# Second time
# Initializing variables
text2 = input("Enter the text2:\n").lower().strip()

for i in non_letters:
    text2 = text2.replace(i, '')

total_occurrences = len(text2)
letter_count = Counter(text2)

# Frequency Analysis Output
print("\nHere is a frequency analysis from the entered text2:")
for k in sorted(letter_count.keys()):
    print(
        f'{k} : {letter_count[k]} = {round(100*letter_count[k]/total_occurrences,2)}%')

ordered_letter_count = letter_count.most_common()

text_ordered_letters = []

for i in ordered_letter_count:
    text_ordered_letters.append(i[0])

print("Letters ordered from highest to lowest frequency:")
for i in text_ordered_letters:
    print(i, end='')
print()
