def main():
    print(get_percentage(get_fraction()))

def get_fraction():
    while True:
        string = input("Fraction: ")
        try:
            x = int(string.split("/")[0])
            y = int(string.split("/")[1])
            if x > y or y == 0:
                pass
            else:
                return x/y
        except ValueError or ZeroDivisionError:
            pass 

def get_percentage(a):
    ans = round(a*100)
    if ans <= 1:
        return "E"
    elif ans >= 99:
        return "F"
    return str(ans) + "%"

main()
