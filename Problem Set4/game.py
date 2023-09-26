from random import randint


def main():
    while True:
        try:
            userrange = int(input("Level: ").strip())
            if userrange >= 1:
                guessme = randint(1, userrange)
                guessed(guessme)
                break

        except (TypeError, ValueError):
            continue


def guessed(gennum):
    while True:
        userguess = int(input("Guess: ").strip())

        try:
            if userguess > gennum:
                print("Too large!")
            elif userguess < gennum:
                print("Too small!")
            else:
                print("Just right!")
                break
        except (TypeError, ValueError):
            continue


if __name__ == "__main__":
    main()
