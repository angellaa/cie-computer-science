searchDate = input("Insert a date: ")

file = open("discount_dates.txt", 'r')

for line in file:
    record = line.split()
    date = record[0]
    discount = record[1]

    if searchDate == date:
        if discount == "TRUE":
            print("This is a discount date")
        else:
            print("No discount on this date")
        exit()

print("Date not found")
