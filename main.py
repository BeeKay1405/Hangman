# Hangman Game
# Author: Akshat Kashyap
# Description: A simple Hangman game implementation in Python.

import game
import wordLoader

category = {1: "Animals",
            2: "Cars",
            3: "Colours",
            4: "Countries",
            5: "Fruits",
            6: "Movies",
            7: "Professions",
            8: "Sports"}

def main():
    game.gameLogic()
    while input("Do you want to keep playing? (Y/N)").upper() == "Y":
        wordCat = int(input("Please select the category of words you want to play."
                            "\n1. Animals"
                            "\n2. Cars"
                            "\n3. Colours"
                            "\n4. Countries"
                            "\n5. Fruits"
                            "\n6. Movies"
                            "\n7. Professions"
                            "\n8. Sports\n"))
        if wordCat not in range(1, 9):
            exit()
        wordLoader.word = wordLoader.getWord(wordCat)
        game.gameLogic()

if __name__ == "__main__":
    main()
