def DisplayMenu():
    print("MENU")
    print(" 1. Read data from the customer file")
    print(" 2. Add a customer")
    print(" 3. Search for a customer")
    print(" 4. Terminates the program")

def ReadFile():
    print("Read file code")


while True:
    i = 3
    DisplayMenu()
    NoOfAttempts = 0
    choice = 0

    while (choice < 1 or choice > 4) and NoOfAttempts < i:
        choice = int(input("Enter choice (1..4): "))
        NoOfAttempts += 1

    if choice == 1:
        ReadFile()
    elif choice == 2:
        print("Add customer code")
    elif choice == 3:
        print("Search customer code")
    elif choice == 4:
        exit()
