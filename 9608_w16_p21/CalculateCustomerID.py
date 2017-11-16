#
#  Variables:
#   - Surname: String
#   - SurnameLength, NextCodeNumber, CustomerID, i: Integer
#   - NextChar: Char
#

Surname = input("Enter your surname: ")
SurnameLength = len(Surname)
CustomerID = 0

for i in range(0, SurnameLength):
    NextChar = Surname[i]
    NextCodeNumber = ord(NextChar)
    CustomerID = CustomerID + NextCodeNumber

print("Customer ID is ", CustomerID)
