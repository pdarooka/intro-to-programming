# Dictionaries: Code Breaker
from collections import Counter

# Welcome message
print("Welcome!")

non_letters = [
    '&', '%', '$', '!', ' ', ',', '.', ' /', '"', '?', '\n', ':',
    '(', ')', ';', '-', '\'', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
]

# First time
# Initializing variables
# text = input("Enter the text:\n").lower().strip()
text = """
To Sherlock Holmes she is always the woman. I have seldom heard him mention her under any other name.
In his eyes she eclipses and predominates the whole of her sex. It was not that he felt any emotion akin to love for Irene Adler.
All emotions, and that one particularly, were abhorrent to his cold, precise but admirably balanced mind.
He was, I take it, the most perfect reasoning and observing machine that the world has seen, but as a lover he would have placed himself in a false position.
He never spoke of the softer passions, save with a gibe and a sneer.
They were admirable things for the observer excellent for drawing the veil from men's motives and actions.
But for the trained reasoner to admit such intrusions into his own delicate and finely adjusted temperament was to introduce
a distracting factor which might throw a doubt upon all his mental results.
Grit in a sensitive instrument, or a crack in one of his own highpower lenses,
would not be more disturbing than a strong emotion in a nature such as his.
And yet there was but one woman to him, and that woman was the late Irene Adler, of dubious and questionable memory.
I had seen little of Holmes lately. My marriage had drifted us away from each other.
My own complete happiness, and the homecentred interests which rise up around the man who first finds himself master of his own establishment,
were sufficient to absorb all my attention, while Holmes, who loathed every form of society with his whole Bohemian soul,
remained in our lodgings in Baker Street, buried among his old books, and alternating from week to week between cocaine and ambition,
the drowsiness of the drug, and the fierce energy of his own keen nature.
He was still, as ever, deeply attracted by the study of crime,
Page 89
and occupied his immense faculties and extraordinary powers of observation in following out those clues,
and clearing up those mysteries which had been abandoned as hopeless by the official police. From time to time I heard some vague account of his doings: of his summons to Odessa in the case of the Trepoff murder,
of his clearing up of the singular tragedy of the Atkinson brothers at Trincomalee,
and finally of the mission which he had accomplished so delicately and successfully for the reigning family of Holland.
Beyond these signs of his activity, however, which I merely shared with all the readers of the daily press, I knew little of my former friend and companion.
"""


for i in non_letters:
    text = text.strip().lower().replace(i, '')

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
# text2 = input("Enter the text2:\n").lower().strip()
text2 = """
Quite so! You have not observed. And yet you have seen.
That is just my point. Now, I know that there are seventeen steps, because I have both seen and observed.
By the way, since you are interested in these little problems,
and since you are good enough to chronicle one or two of my trifling experiences, you may be interested in this.
He threw over a sheet of thick, pink tinted notepaper which had been lying open upon the table. It came by the last post, said he. Read it aloud.
The note was undated, and without either signature or address.
There will call upon you tonight, at a quarter to eight o'clock,
it said, "a gentleman who desires to consult you upon a matter of the very deepest moment. Your recent services to one of the royal houses of Europe have shown that you are one who may safely be trusted
with matters which are of an importance which can hardly be exaggerated.
This account of you we have from all quarters received.
Be in your chamber then at that hour, and do not take it amiss if your visitor wear a mask.
This is indeed a mystery, I remarked. What do you imagine that it means?
I have no data yet. It is a capital mistake to theorise before one has data.
Insensibly one begins to twist facts to suit theories, instead of theories to suit facts.
But the note itself. What do you deduce from it?
I carefully examined the writing, and the paper upon which it was written.
The man who wrote it was presumably well to do, I remarked, endeavouring to imitate my companion's processes.
Such paper could not be bought under half a crown a packet.
It is peculiarly strong and stiff.
"""

for i in non_letters:
    text2 = text2.strip().lower().replace(i, '')

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

# Gets user input
en_dec = input("Would you like to encode or decode a message? ").lower().strip()

text_new = input("Enter the text2:\n").lower().strip()
for i in non_letters:
    text_new = text_new.replace(i, '')

if en_dec == 'encode':
    encoded_ = []
    for letter in text_new:
        index = text_ordered_letters2.index(letter)
        charac = text_ordered_letters[index]
        encoded_.append(charac)
    
    for letter in encoded_:
        print(letter, end='')

elif en_dec == 'decode':
    decoded_ = []
    for letter in text_new:
        index = text_ordered_letters.index(letter)
        charac = text_ordered_letters2[index]
        decoded_.append(charac)

    for letter in decoded_:
        print(letter, end='')

else:
    print("Invalid input.")