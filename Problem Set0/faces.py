def main():
    string = input()
    if ":)" and ":(" in string:
        print(both(string))
    elif ":)" in string:
        print(happy(string))
    elif ":(" in string:
        print(sad(string))


def happy(s):
    return s.replace(":)","🙂")

def sad(s):
    return s.replace(":(","🙁")

def both(s):
    return s.replace(":)","🙂").replace(":(","🙁")

main()
