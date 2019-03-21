speedLimit = 70
driverSpeed = 170
speedDiff = driverSpeed - speedLimit
demerit = speedDiff / 5

def checkSpeed(speedLimit):
    if speedLimit <= 70:
        print("Your speed is okay!")
    else:
        print("You are speeding...slow down!")
        print("Miles over the speed limit: " + str(speedDiff))
        print("Points on license: " + str(demerit))
        if(demerit >= 12):
            print("You're too reckless to be driving, your license is suspended!")      

checkSpeed(driverSpeed)
