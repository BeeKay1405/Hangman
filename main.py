import game


def main():
    game.gameLogic()
    while input("Do you want to keep playing? (Y/N)").upper() == "Y":
        wordCat = int(input("Welcome!\nPlease select the category of words you want to play.\n1. Movies\n2. Cars\n"))
        if wordCat not in range(1, 3):
            exit()



if __name__ == "__main__":
    main()
