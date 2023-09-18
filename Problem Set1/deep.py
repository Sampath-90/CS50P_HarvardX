def main():
    string = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
    if is_true(string):
        print("Yes")
    else:
        print("No")

def is_true(s):
    match s:
        case "42"| "forty two" | "forty-two":
            return True
        case _:
            return False

main()
