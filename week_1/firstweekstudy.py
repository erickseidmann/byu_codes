# import the math module so i can use math.pi and math.sqrt
import math 

# print a description of this progrma for the user to see.
print ( " this program computes and outpus the")
print (" surface area of a right circular cone.")

# get the ridus and the height from the user.
radius = float(input("Enter the radius of a cone: "))
height = float(input("Enter the height of a cone: "))

# compute the surface are of the cone.

radical = math.sqrt(radius**2 + height**2)
surf_area= math.pi * radius * (radius + radical)

# round the surface area to one digit after the decimal point.
surf_area = round(surf_area, 1)


# print the surface area for the user to see. 
print(f"The surface area is {surf_area}")