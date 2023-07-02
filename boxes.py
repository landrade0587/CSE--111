"""
File: boxes.txt
Author: Luis Andrade
Date: 11 January 2023
Purpose: Checkpoint: Calling Functions.
"""
import math

# Brief information or presentation for the user
print( """ \n\n\n 
+============================================+
|                                            |
|    ¡Welcome to computes two integer:       |
|      the number of manufactured            |
|    and the number of items for box.        |
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

# User-entered values
items_number = int(input(f"\n\n\nPlease first enter the number of items: "))
box_per_items = int(input(f"Please Second enter the number of items per box: "))

# compute the numbers of the boxes
boxes_numbers = math.ceil(items_number / box_per_items)

# Display the results for the user to see.
print(f"\n\nFor {items_number} items, packing {box_per_items}"
     "\nitems in each box,"
     f"\nyou will need {boxes_numbers} boxes.")

print("\n\n Thanks for participating.")
