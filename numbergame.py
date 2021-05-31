n = 15
chances = 4

while chances >= 0:
    m = int(input("Enter your choice to guess the number"))

    if chances > 0 and m != n:
        if m < n:
            print("you guess the less number")
        elif m > n:
            print("you guessed the greater number")

        else:
            print("you won")
            break
        print("you have only", chances , "left")
    elif chances == 0 and m != n:
        print("aata naa jaata bade aae khelne wale")
        print("chalo ab dusre ko khelne do")

    chances = chances-1
