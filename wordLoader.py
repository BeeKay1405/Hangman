import random


# Asks the user which category of words they want to play.

wordCat = int(input("Welcome!\nPlease select the category of words you want to play.\n1. Movies\n2. Cars\n"))
if wordCat not in range(1, 3):
    exit()


# Chooses a random word from the text file of the category of words.

def getWord(wordCat):
    if wordCat == 1:
        file = open("movies.txt")
    elif wordCat == 2:
        file = open("cars.txt")
    else:
        exit()
    wordList = file.read().split("\n")
    word = random.choice(wordList)
    return word

word = getWord(wordCat)
# Converts the word into underscore form (except special symbols)

def wordBlanks(word):
    wordDisplay = ''
    for char in word:
        if char.isalnum():
            wordDisplay += '_'
        else:
            wordDisplay += char
    return wordDisplay
