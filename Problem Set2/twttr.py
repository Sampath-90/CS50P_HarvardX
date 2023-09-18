def main():
    string = input("Input: ")
    print(check(string))

def check(s):
    vowels = ['a','e','i','o','u']
    for char in s:
        if char.casefold() in vowels:
            s = s.replace(char,"")
    return s

main()
