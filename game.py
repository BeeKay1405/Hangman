import wordLoader
from hangMan import stages


# Main game function

def gameLogic():
    word = wordLoader.getWord().upper()
    wordCompletion = wordLoader.wordBlanks()
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
        if len(guess) == 1 and guess.isalnum():
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
                for index in indices:
                    wordAsList[index] = guess
                wordCompletion = ''.join(wordAsList)
                if '_' not in wordCompletion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalnum():
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
        print("You now have", tries, "tries left")
        if tries == 0:
            print("The word was", word)
        else:
            print(wordCompletion)
        print(stages[tries])
        print("\n")
        if guessed:
             print("You Win")
