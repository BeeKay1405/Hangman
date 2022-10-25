import random

# Asks the user which category of words they want to play.

wordCat = int(input("Welcome!\nPlease select the category of words you want to play.\n1. Movies\n2. Cars\n"))
if wordCat not in range(1, 3):
    exit()


# Chooses a random word from the text file of the category of words.

def getWord():
    if wordCat == 1:
        file = open("movies.txt")
    elif wordCat == 2:
        file = open("cars.txt")
    else:
        exit()
    wordList = file.read().split("\n")
    word = random.choice(wordList)
    return word


# Converts the word into underscore form (except special symbols)

def wordBlanks():
    wordDisplay = ''
    for char in getWord():
        if char.isalnum():
            wordDisplay += '_'
        else:
            wordDisplay += char
    return wordDisplay
