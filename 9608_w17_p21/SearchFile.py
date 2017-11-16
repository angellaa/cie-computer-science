#
# Variables:
#   - searchUserId : string
#   - index : integer
#   - userId, portId, timeAndDate : string
#   - file : file
#

def SearchFile():
    searchUserId = input("Insert a user ID: ")
    index = 0
    file = open("LoginFile.txt")

    for line in file:
        userId = line[:5]
        portId = line[5:9]
        timeAndDate = line[9:]

        if userId == searchUserId:
            loginEvents[index][0] = portId
            loginEvents[index][1] = timeAndDate
            index = index + 1

    file.close()

# Initialize LogEvents before calling SearchFile
loginEvents = a = [[""] * 2 for i in range(10)]  # We use 10 for simplicity instead of 1000

SearchFile()

print(loginEvents)
