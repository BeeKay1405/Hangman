import random

category = {
    1: "Animals",
    2: "Cars",
    3: "Colours",
    4: "Countries",
    5: "Fruits",
    6: "Movies",
    7: "Professions",
    8: "Sports"
}


file_names = {
    1: "animals.txt",
    2: "cars.txt",
    3: "colours.txt",
    4: "countries.txt",
    5: "fruits.txt",
    6: "movies.txt",
    7: "professions.txt",
    8: "sports.txt"
}


def getDifficulty():
    while True:
        try:
            difficulty = int(input("Which difficulty would you like to play in?"
                                   "\n1. Easy"
                                   "\n2. Medium"
                                   "\n3. Hard\n"))
            if difficulty in range(1, 4):
                return difficulty
            else:
                print("Invalid input! Please enter a valid difficulty level.")
        except ValueError:
            print("Invalid input! Please enter a valid difficulty level.")


def getWord(wordCat):
    if wordCat in file_names:
        file = open(file_names[wordCat])
    else:
        exit(1)
    wordList = file.read().split("\n")
    easyWords = [word for word in wordList if len(word) <= 5]
    mediumWords = [word for word in wordList if len(word) > 5 and len(word) <= 10]
    hardWords = [word for word in wordList if len(word) > 10]
    filteredWords = {1: easyWords, 2: mediumWords, 3: hardWords}

    if not filteredWords[1] and not filteredWords[2] and not filteredWords[3]:
        print("No words available in this category.")
        exit(1)

    if hardWords:
        difficulty = getDifficulty()
    else:
        difficulty = getDifficulty()
        if difficulty == 3:
            print("No hard words available in this category.")
            exit(1)

    return random.choice(filteredWords[difficulty])


def selectCategory():
    wordCat = int(input("Please select the category of words you want to play."
                        "\n1. Animals"
                        "\n2. Cars"
                        "\n3. Colours"
                        "\n4. Countries"
                        "\n5. Fruits"
                        "\n6. Movies"
                        "\n7. Professions"
                        "\n8. Sports\n"))

    if wordCat not in category:
        print("Invalid category selection!")
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
    return category[wordCat]
