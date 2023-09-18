def main():
    string = input("Greeting: ").strip()
    print(greeting(string))


def greeting(s):
    if "Hello" in s.split()[0]:
        return "$0"
    elif "H" in s.split()[0][0]:
        return "$20"
    else:
        return "$100"


main()
