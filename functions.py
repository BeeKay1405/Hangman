import random

yellow = '\033[33m'
green = '\033[32m'
red = '\033[31m'
blue = '\033[34m'
white = '\033[0m'

categories = {
    1: "animals",
    2: "cars",
    3: "colours",
    4: "countries",
    5: "fruits",
    6: "movies",
    7: "professions",
    8: "sports",
    9: "multiplayer"
}

fileNames = {
    1: "animals.txt",
    2: "cars.txt",
    3: "colours.txt",
    4: "countries.txt",
    5: "fruits.txt",
    6: "movies.txt",
    7: "professions.txt",
    8: "sports.txt"
}

difficulties = {
    1: 'Easy',
    2: 'Medium',
    3: 'Hard'
}


def getDifficulty():
    while True:
        try:
            difficulty = int(input(green + "Which difficulty would you like to play in?"
                                           "\n1. Easy"
                                           "\n2. Medium"
                                           "\n3. Hard\n" + white))
            if difficulty in range(1, 4):
                return difficulty
            else:
                print(red + "Invalid input! Please enter a valid difficulty level." + white)
        except ValueError:
            print(red + "Invalid input! Please enter a valid difficulty level." + white)


def getWord(wordCat, conn):
    try:
        cursor = conn.cursor()

        if wordCat in categories:
            category = categories[wordCat]
        else:
            print(red + "Invalid category!" + white)
            return None

        wordTuple = cursor.execute("SELECT word FROM WORDS WHERE category = ? ", (category,), ).fetchall()

        if wordTuple is not None:
            word = (random.choice(wordTuple)[0])
        else:
            print(red + "No words available in this category." + white)
            return None

        while True:
            difficulty = getDifficulty()
            wordCount = cursor.execute("SELECT COUNT(*) FROM WORDS WHERE category = ? AND difficulty = ?",
                                       (category, difficulties[difficulty],), ).fetchall()

            if not wordCount:
                print(red + "This difficulty of words is not available in this category. "
                            "Please select another difficulty" + white)
                continue
            break

        return word

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def getPlayerName():
    playerName = str(input(green + "Please enter you name or input 0 if you want to play anonymously:\n" + white))
    if playerName == '0':
        return 0
    else:
        return playerName


def selectCategory():
    wordCat = int(input(green + "Please select the category of words you want to play."
                                "\n1. Animals"
                                "\n2. Cars"
                                "\n3. Colours"
                                "\n4. Countries"
                                "\n5. Fruits"
                                "\n6. Movies"
                                "\n7. Professions"
                                "\n8. Sports"
                                "\n9. Multiplayer\n" + white))

    if wordCat not in categories:
        print(red + "Invalid category selection!" + white)
        return selectCategory()

    return wordCat


def wordBlanks(word):
    wordDisplay = ''
    for char in word:
        if char.isalnum():
            wordDisplay += '_'
        else:
            wordDisplay += char
    return wordDisplay


def getCategoryName(wordCat):
    return categories[wordCat]


def scoreLogic(guessType):
    global score
    try:
        score
    except NameError:
        score = 0
    if guessType == 0:
        pass
    elif guessType == 1:
        score += 1
    elif guessType == 2:
        score += 3
    else:
        score += 5

    return score


def writeLeaderboard(name, score):
    if name != 0:
        with open("leaderboard.txt", "a") as file:
            file.write(f"{name}: {score}\n")
    else:
        with open("leaderboard.txt", "a") as file:
            file.write(f"Anonymous: {score}\n")


def printLeaderboard():
    with open("leaderboard.txt", "r") as file:
        leaderboard = file.readlines()

    leaderboard = [line.strip().split(":") for line in leaderboard]
    sortedLeaderboard = sorted(leaderboard, key=lambda x: int(x[1]) if len(x) >= 2 else 0, reverse=True)

    print(yellow + "Leaderboard:")
    for entry in sortedLeaderboard:
        print(f"Name: {entry[0]}, Score: {entry[1]}")


def hint(wordAsList, word, guessedLetters):
    indices = [i for i, char in enumerate(wordAsList) if char == '_']
    index = random.choice(indices)
    letterIndices = [i for i, char in enumerate(word) if char == word[index]]
    for letterIndex in letterIndices:
        wordAsList[letterIndex] = word[letterIndex]
    guessedLetters.append(word[index])
    return wordAsList, word


def multiplayer():
    userWord = input(green + "Enter the word you want the other player to guess. (Ask them to look away!)\n")
    return userWord


def timer(timeTaken):
    timeFormat = str(int(timeTaken) % 60)
    a = str((int(timeTaken) % 3600) // 60)
    if int(timeTaken) >= 60:
        timeFormat = str((int(timeTaken) % 3600) // 60) + ':' + timeFormat
    if int(timeTaken) >= 3600:
        timeFormat = str(int(timeTaken) // 3600) + ':' + timeFormat
    return timeFormat
