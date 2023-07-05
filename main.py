# Hangman Game
# Author: Akshat Kashyap
# Description: A simple Hangman game implementation in Python.

import game
import wordLoader


def main():
    while True:
        game.gameLogic()
        play_again = input("Do you want to play again? (Y/N): ")
        if play_again.upper() != "Y":
            wordLoader.writeLeaderboard(wordLoader.playerName(), wordLoader.score)
            wordLoader.printLeaderboard()
            break

if __name__ == "__main__":
    main()
