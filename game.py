import sqlite3
import functions
import os
import time
from hangMan import stages
conn = sqlite3.connect('hangman.db')


# Main game function
def gameLogic():
    hintFinish = False
    hintCounter = 0
    wordCat = functions.selectCategory()
    if wordCat == 9:
        categoryName = "Custom"
        functions.word = functions.multiplayer().upper()
        word = functions.word.upper()
    else:
        categoryName = functions.getCategoryName(wordCat)
        functions.word = functions.getWord(wordCat, conn)
        word = functions.word.upper()
    wordCompletion = functions.wordBlanks(functions.word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    tries = 6
    os.system('cls')
    print("Score: ", functions.yellow + str(functions.scoreLogic(0)) + functions.white)
    print("Category: ", functions.yellow + categoryName + functions.white)
    print("You have", functions.yellow + str(tries) + functions.white, "tries left")
    print(functions.yellow + wordCompletion + functions.white)
    print(functions.blue + stages[tries] + functions.white)
    startTime = time.time()
    print("\n")

    while not guessed and tries > 0:
        guess = input(functions.green + "Please guess a letter or a word: " + functions.white).upper()

        if len(guess) == 1 and guess.isalnum():  # Logic for when the player guesses a letter
            if guess in guessedLetters:
                print(functions.red + "You already guessed the letter", guess + functions.white)
            elif guess not in word:
                print(functions.red + guess, "is not in the word" + functions.white)
                tries -= 1
                guessedLetters.append(guess)
            else:
                print(functions.green + "Nice!", guess, "is in the word" + functions.white)
                functions.score = functions.scoreLogic(1)
                guessedLetters.append(guess)
                wordAsList = list(wordCompletion)
                indices = [i for i, letter in enumerate(word) if letter == guess]

                for index in indices:
                    wordAsList[index] = guess
                wordCompletion = ''.join(wordAsList)

                if '_' not in wordCompletion:
                    guessed = True
        elif len(guess) == len(word):  # Logic for when the player guesses a word
            if guess in guessedWords:
                print(functions.red + "You have already guessed this word" + functions.white)
            elif guess != word:
                print(functions.red + guess, "is not the word" + functions.white)
                tries -= 1
                guessedWords.append(guess)
            else:
                guessed = True
                wordCompletion = word
                functions.score = functions.scoreLogic(2)
        else:
            print(functions.red + "Not a valid input" + functions.white)

        if not guessed:
            if ((6 - tries) == 2 and hintCounter == 0) or ((6 - tries) == 4 and hintCounter <= 1):
                hintChoice = input(functions.green + "Would you like a hint? (Y/N): " + functions.white)
                hintCounter += 1
                if hintChoice.upper() == 'Y':
                    functions.score -= 1
                    wordAsList, word = functions.hint(list(wordCompletion), word, guessedLetters)
                    wordCompletion = ''.join(wordAsList)
                    if wordCompletion == word:
                        guessed = True
                        hintFinish = True
            os.system('cls')
            print("Score: ", functions.yellow + str(functions.scoreLogic(0)) + functions.white)
            print("Category:", functions.yellow + categoryName + functions.white)
            print("You now have", functions.yellow + str(tries) + functions.white, "tries left")
            print("Letters guessed:", functions.yellow + str(guessedLetters) + functions.white)
            print("Words guessed:", functions.yellow + str(guessedWords) + functions.white)

        if tries == 0:
            print(functions.green + "The word was", functions.yellow + word + functions.white)
        else:
            print(functions.yellow + wordCompletion + functions.white)

        print(functions.blue + stages[tries] + functions.white)
        print("\n")

    if hintFinish:
        functions.score -= 20

    if guessed:
        endTime = time.time()
        timeTaken = int(endTime - startTime)
        functions.score = functions.scoreLogic(3)
        functions.score = functions.scoreLogic(4, timeTaken)
        print(functions.green + "Congratulations! You Win!" + functions.white)
        print("Score: ", functions.yellow + str(functions.score) + functions.white)
        print("Time Taken: ", functions.yellow + str(timeTaken) + functions.white)
    else:
        print(functions.red + "Sorry, you lost." + functions.white)
