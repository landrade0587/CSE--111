"""
File: tired_volume.txt
Author: Luis Andrade
Date: 14 January 2023
Purpose: Prove Milestone: Review Python.
"""
import math

# Brief information or presentation for the user
print( """ \n\n\n 
+============================================+
|                                            |
|     ¡Welcome to computes and outputs       |
|  the volume of space inside that tire.!    |
|                                            |
+============================================+""")

# A wait activation to make the wait pleasant
print( "\n\n  Please stay one moment please... " )

import time
for second in range(1, 4):
    print(second, "Second")
    time.sleep(1)
print("Are you Ready?")	
print("Ready or not, here I come!")

# More information to the user so that he understands what the program will do
print("""\n\n
 I¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯I
 º                                                   º
 º       This program collect the information        º
 º         that reads from the keyboard              º
 º          the three numbers for a tire             º
 º         and computes and outputs the volume       º
 º            of space inside that tire.             º
 º                                                   º
 I¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯I""")

# User-entered values
print("\n\n Please enter the values of the tired:")
width = int(input("First please enter the width of the tire in millimeters: "))
aspect_ratio = int(input("Second please enter the aspect ratio: "))
diameter = int(input("Third please enter the diameter in inches of the wheel that fits the tire: "))

# Compute the volume of space inside that tire
v1 = (width**2)*(aspect_ratio)
v2 = (width*aspect_ratio + 2540*diameter)
v3 = 10000000000

volume = math.pi*v1*v2/v3

# Print the volume of space inside that tired
print(f"\n The volume of space inside that tired is: {volume:.2f} liters.")

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Use an f-string to print only the date
# part of the current date and time.
print(f"Today is: {current_date_and_time:%Y-%m-%d}")

print("\n Thanks for participating.")

# Open a text file named volumes.txt in append mode.
with open("volumes.txt", "at") as volume_file:

    # Print a volumes and information to the file.
    print(f"{current_date_and_time:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}", file=volume_file)  