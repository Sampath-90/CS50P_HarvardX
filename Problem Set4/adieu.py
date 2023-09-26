import inflect


def main():
    p = inflect.engine()
    mylist = []

    while True:
        try:
            user_input = str(input("Name: ")).strip()
            mylist.append(user_input)
        except (EOFError, KeyError):
            print(f"Adieu, adieu, to {p.join(mylist)}", end="\n")
            quit()


if __name__ == "__main__":
    main()
