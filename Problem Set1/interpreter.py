def main():
    string = input("Expression: ").strip().split(" ")
    x = float(string[0])
    y = string[1]
    z = float(string[2])
    print(calc(x,y,z))

def calc(x,y,z):
    match y:
        case "+":
            return round(x+z,1)
        case "-":
            return round(x-z,1)
        case "/":
            return round(x/z,1)
        case "*":
            return round(x*z,1)

main()
