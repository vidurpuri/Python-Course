a = int(input("Enter a number between 1 and 10: "))

match a:
    case 1:
        print("You entered one.")
    case 2:
        print("You entered two.")
    case 3:
        print("You entered three.")
    case 4:
        print("You entered four.")
    case 5:
        print("You entered five.")
    case 6:
        print("You entered six.")
    case 7:
        print("You entered seven.")
    case 8:
        print("You entered eight.")
    case 9:
        print("You entered nine.")
    case 10:
        print("You entered ten.")
    case _:
        print("Invalid input.")
