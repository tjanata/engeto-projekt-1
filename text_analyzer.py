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
Text_index = []


# User´s input
username = input("username:")
password = input("password:")


# Verify if user is registered
if username in users and users[username] == password:
    print(oddelovac)
    print(f"Welcome to the app, {username}")
    print(f"We have 3 texts to be analyzed.")
    print(oddelovac)

    # Get number of selected text from user
    selected_text = input("Enter a number btw. 1 and 3 to select: ")
    print(oddelovac)

    # Get number of text from TEXTS
    for text in range(len(TEXTS)):
        number_of_text = text + 1
        Text_index.append(number_of_text)
    
    if selected_text.isnumeric() and int(selected_text) in Text_index:
            # Get index of items in list
            index = int(selected_text) - 1
            words = TEXTS[index].split()

            # Count words in selected text
            word_count = len(words)
            print(f"There are {word_count} words in the selected text.")
            
            # Count words with capital character
            capital_world = 0
            for word in words:
                if word.istitle():
                    capital_world += 1
            print (f"There are {capital_world} titlecase words.")

            # Count words with uppercase character only
            uppercase_word = 0
            for word in words:
                 if word.isupper():
                      uppercase_word += 1
            print(f"There are {uppercase_word} uppercase words.")

            # Count words with lower characters
            lower_word = 0
            for word in words:
                 if word.islower():
                      lower_word += 1
            print(f"There are {lower_word} lowercase words.")

            # Count numeric words
            numeric_word = 0
            for word in words:
                 if word.isdigit():
                      numeric_word += 1
            print(f"There are {numeric_word} numeric strings.")

            # Suma of numbers
            suma = 0
            for word in words:
                if word.isdigit():
                    suma += int(word)
            print(f"The sum of all the numbers {suma}.")


        
    else:
            print("bad input, terminating the program..")


else:
    print(f"unregistered user, terminating the program..")

