"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tomas Janata
email: tomas.janata@nempk.cz
discord: TomášJ#3088
"""


# Variables
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
oddelovac = "----------------------------------------"
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
text_index = []

capital_word_count = 0
uppercase_word_count = 0
lowercase_word_count = 0
numeric_word_count = 0
sum_of_numbers = 0


# User´s input
username = input("username:")
password = input("password:")


# Verify if user is registered
if username in users and users[username] == password:
    print(oddelovac)
    print(f"Welcome to the app, {username}")
    print(f"We have 3 texts to be analyzed.")
    print(oddelovac)

else:
    print(f"unregistered user, terminating the program..")
    quit()


# Get number of selected text from user
selected_text = input("Enter a number btw. 1 and 3 to select: ")
print(oddelovac)


# Get number of text from TEXTS (adding indexes of individual items from the variable TEXTS to new variable text_index)
for text in range(len(TEXTS)):
    number_of_text = text + 1
    text_index.append(number_of_text)

if int(selected_text) not in text_index:
    print("bad input, terminating the program..")
    quit()

else:
    print(f"Your selected text is {selected_text}")


# Get values from TEXTS
if int(selected_text) not in text_index:
    quit()

elif selected_text.isnumeric():

    # Get index of items in list
    index = int(selected_text) - 1
    words = TEXTS[index].split()

    # Count words in selected text
    word_count = len(words)
    print(f"There are {word_count} words in the selected text.")

    # Count other result from selected text
    for word in words:
        if word.istitle():
            capital_word_count += 1
        elif word.isupper():
            uppercase_word_count += 1
        elif word.islower():
            lowercase_word_count += 1
        elif word.isdigit():
            numeric_word_count += 1
            sum_of_numbers += int(word)

    print(f"There are {capital_word_count} titlecase words.")
    print(f"There are {uppercase_word_count} uppercase words.")
    print(f"There are {lowercase_word_count} lowercase words.")
    print(f"There are {numeric_word_count} numeric strings.")
    print(f"The sum of all the numbers: {sum_of_numbers}.")
    print(oddelovac)
    print(f"LEN|    OCCURENCES    |NR.")
    print(oddelovac)


    # Create graph
    word_lengths = {}

    for word in words:
        length = len(word)
        if length in word_lengths:
            word_lengths[length] += 1
        else:
            word_lengths[length] = 1

    sorted_lengths = sorted(word_lengths.items())
    max_length = max(word_lengths.keys())

    for item_2 in range(1, max_length + 1):
        if item_2 in word_lengths:
            bar = '*' * word_lengths[item_2]
            print(f"{item_2:2d}|{bar: <19}|{word_lengths[item_2]}")
        else:
            print(f"{item_2:2d}|{'': <19}|0")
else:
    print("Invalid input. Terminating the program...")
    quit()
