# name = input("Please enter your name: ")
# print(f"Hello {name}")

#n = float(input("Please enter a number: "))
#r = round(n, 2)
#print(r)


#import math

#r = math.sqrt(71)
#print(r)

# Example 6

# Get a string of text from the user.
#text1 = input("Enter a motivational quote: ")

# Call the built-in len function to get
# the number of characters in the text.
#length = len(text1)

# Call the string upper method to convert
# the quote to upper case characters.
#text2 = text1.upper()

# Call the built-in print function to print
# the length of the text and the text in all
# upper case for the user to see.
# print(length, text2)

# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

"""
A manufacturing company needs a program that will help its employees
pack manufactured items into boxes for shipping. Write a Python
program named boxes.py that asks the user for two integers:  1) the
number of manufactured items and 2) the number of items that the user
will pack per box. Your program must compute and print the number of
boxes necessary to hold the items. This must be a whole number. Note
that the last box may be packed with fewer items than the other boxes.
"""

# Import the math module so that we can call the math.ceil function.
import math

# Get two numbers from the user.
num_items = int(input(f"Enter the number of items: "))
items_per_box = int(input(f"Enter the number of items per box: "))

# Compute the number of boxes by dividing
# and then calling the math.ceil function.
num_boxes = math.ceil(num_items / items_per_box)

# Display a blank line.
print()

# Display the results for the user to see.
print(f"For {num_items} items, packing {items_per_box}"
    f" items in each box, you will need {num_boxes} boxes.")


    