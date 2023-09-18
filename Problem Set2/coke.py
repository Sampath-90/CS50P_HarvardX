def main():
    a = 50
    i = None
    while a > 0:
        string = "Amount Due: " + str(a)
        print(string)
        i = int(input("Insert Coin: "))
        if insert_coin(i):
            a -= i
    print("Change Owed: " + str(abs(a)))

def insert_coin(i):
    valid = ['5','10','25']
    if str(i) in valid:
        return True

main()
