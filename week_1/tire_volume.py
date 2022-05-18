import math
#description of this program 
name = input("Hello, what's your name? ")
print("welcome " + name + ", with this program we are going to")
print("get the tire volume, please enyoy it!")
print()

# Geting the information: with/ aspect /diameter
width = float(input(name + ", please enter the width of the tire in mm (ex 205): "))
print()
aspect = float(input(name + ", please enter the aspect ratio of the tire (ex 60): "))
print()
diameter = float(input(name + ", please enter the diameter of the wheel in inches (ex 15): "))
print()

# compute the tire volume
tire_volume = math.pi * width*width * aspect *(width * aspect + 2540 * diameter) / (10000000000)

# round the tire volume to tow digits after the decimal point.
tire_volume = round(tire_volume, 2)

#date
from datetime import datetime, timedelta
today = datetime.now()

print(f"{name} the approximate volume is {tire_volume} liters")
print()
question = input(name + " Would you like to see more codes today?(yes/no) ")

if question =="yes":
    print()
    print("Great "+ name +" so let's continue!")
    print()
    second_question = input(name +", do you know the date and time now?(yes/no) ")
    print()
else:
    print(":C, no problem, I understand, so see you next time!" )

if second_question == "yes":
    print("exactly " + name + " today is:" + str(today))
    
else:
    print("No problem I can tell you the date and time now is: "+ str(today))
    third_question = input ("excellent now let's save all this information we got in a file?(yes/no) ")


# Appends to the end of the volumes.txt file one line of text that contains the following five values:

print(name +",  let's go! Now you just need to find a file called -volumes txt-, and see all the information we used in this activity! ")
current_date = today
width_of_the_tire = width
aspect_ratio = aspect
diameter_of_the_wheel = diameter
volume_of_the_tire = tire_volume
with open("volumes.txt", "at") as volumes_txt:
    print(name, file=volumes_txt)
    print(current_date, file=volumes_txt)
    print(width_of_the_tire, file=volumes_txt)
    print(aspect_ratio, file=volumes_txt)
    print(diameter_of_the_wheel, file=volumes_txt)
    print(volume_of_the_tire, file=volumes_txt)
