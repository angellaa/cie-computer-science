RaceHours = int(input("Insert race time hours: "))
RaceMinutes = int(input("Insert race time minutes: "))
RaceSeconds = int(input("Insert race time seconds: "))

PersonalBestTime = int(input("Insert your personal best time (in seconds): "))

RaceTime = RaceSeconds + 60 * (RaceMinutes + 60 * RaceHours)

print("Race time in seconds: {}".format(RaceTime))

if RaceTime < PersonalBestTime:
    print("Personal best time is unchanged")
elif RaceTime > PersonalBestTime:
    print("New personal best time")
else:
    print("Equals personal best time")

