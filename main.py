# Hangman Game
# Author: Akshat Kashyap
# Description: A simple Hangman game implementation in Python.

import game
import wordLoader


def main():
    while True:
        game.gameLogic()
        playAgain = input("Do you want to play again? (Y/N): ")
        if playAgain.upper() != "Y":
            wordLoader.writeLeaderboard(wordLoader.getPlayerName(), wordLoader.score)
            wordLoader.printLeaderboard()
            break


if __name__ == "__main__":
    main()
