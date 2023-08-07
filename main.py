# Hangman Game
# Author: Akshat Kashyap
# Description: A simple Hangman game implementation in Python.

import game
import functions


def main():
    while True:
        game.gameLogic()
        playAgain = input(functions.green + "Do you want to play again? (Y/N): ")
        if playAgain.upper() != "Y":
            functions.writeLeaderboard(functions.getPlayerName(), functions.score)
            functions.printLeaderboard()
            break


if __name__ == "__main__":
    main()
