import wordLoader
from hangMan import stages


# Main game function
def gameLogic():
    wordCat = wordLoader.selectCategory()
    categoryName = wordLoader.getCategoryName(wordCat)
    wordLoader.word = wordLoader.getWord(wordCat)
    word = wordLoader.word.upper()
    wordCompletion = wordLoader.wordBlanks(wordLoader.word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    tries = 6
    print("Score: ", wordLoader.scoreLogic(0))
    print("Category: " + categoryName)
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
                wordLoader.score = wordLoader.scoreLogic(1)
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
                print("You have already guessed this word")
            elif guess != word:
                print(guess, "is not the word")
                tries -= 1
                guessedWords.append(guess)
            else:
                guessed = True
                wordCompletion = word
                wordLoader.score = wordLoader.scoreLogic(2)
        else:
            print("Not a valid input")

        if not guessed:
            print("Score: ", wordLoader.scoreLogic(0))
            print("Category:", categoryName)
            print("You now have", tries, "tries left")
            print("Letters guessed:", guessedLetters)
            print("Words guessed:", guessedWords)

        if tries == 0:
            print("The word was", word)
        else:
            print(wordCompletion)

        print(stages[tries])
        print("\n")

    if guessed:
        wordLoader.score = wordLoader.scoreLogic(3)
        print("Congratulations! You Win!")
        print("Score: ", wordLoader.score)
    else:
        print("Sorry, you lost.")
