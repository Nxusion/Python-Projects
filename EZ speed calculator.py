print("###################################################")
print("EZ-speed calculator ROADTRIP EDITION OS version 1.01")
print("Powered by python IDE engine")
print("###################################################")
print("")
# Program start
miles = input("How far was your trip in miles? ")
hours = input("How many hours did it take? ")

# should convert string entry into integers or else it will not work
miles = int(miles)
hours = int(hours)

# Do the math
speed = miles / hours

# Convert again
speed = str(speed)

# Export answer
print("")
print("Your speed was " + speed + " miles per hour.")