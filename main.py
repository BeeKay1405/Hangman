import game


def main():
    game.gameLogic()
    while input("Do you want to keep playing? (Y/N)").upper() == "Y":
        game.gameLogic()


if __name__ == "__main__":
    main()
