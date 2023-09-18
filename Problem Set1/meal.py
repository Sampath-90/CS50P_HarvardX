def main():
    string = input("What time is it? ").strip()
    meal = convert(string)
    print(t(meal))

def convert(time):
    minute = (round((float(time.split(":")[1])/6),1))/10
    return (float(time.split(":")[0])+minute)

def t(m):
    if 7 <= m <= 8:
        return "breakfast time"
    elif 12 <= m <= 13:
        return "lunch time"
    elif 18 <= m <= 19:
        return "dinner time"
    else:
        return ""

if __name__ == "__main__":
    main()
