import main
import wordLoader
from hangMan import stages


# Main game function

def gameLogic():
    word = wordLoader.word.upper()
    wordCompletion = wordLoader.wordBlanks(wordLoader.word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    tries = 6
    print("You have", tries, "tries left")
    print(wordCompletion)
    print(stages[tries])
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalnum():  # Logic for when the player guesses a letter
            if guess in guessedLetters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                tries -= 1
                guessedLetters.append(guess)
            else:
                print("Nice!", guess, "is in the word")
                guessedLetters.append(guess)
                wordAsList = list(wordCompletion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                '''Makes a list of indices corresponding to
                to correct guesses. These indices are used for the following lines of code'''
                for index in indices:
                    wordAsList[index] = guess
                wordCompletion = ''.join(wordAsList)
                ''' This else block is for the case when the player guesses the letter correctly.
                The correct guesses are replaced with the underscores'''
                if '_' not in wordCompletion:
                    guessed = True
        elif len(guess) == len(word):  # Logic for when the player guesses a word
            if guess in guessedWords:
                print("You have already guessed this word")
            elif guess != word:
                print(guess, "is not the word")
                tries -= 1
                guessedWords.append(guess)
            else:
                guessed = True
                wordCompletion = word
        else:
            print("Not a valid input")
        if not guessed:
            print("You now have", tries, "tries left")
            print("Letters guessed: ",guessedLetters)
            print("Words guessed: ",guessedWords)
        if tries == 0:
            print("The word was", word)
        else:
            print(wordCompletion)
        print(stages[tries])
        print("\n")
        if guessed:
             print("You Win")
