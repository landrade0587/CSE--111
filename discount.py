"""
File: discount.txt
Author: Luis Andrade - Gabriel, Henrietta Divine
Date: 11 January 2023
Purpose: Team Activity: Calling Functions.
"""

# Import the datetime class from the datetime
# module so that it can be used in this program
from datetime import datetime
import time

# We include a timer.
for second in range(1, 4):
    print(second, "Second")
    time.sleep(1)
print("Are you Ready?")	
print("Ready or not, here I come!")

# we include the percentage values.
rate_discount = 0.10
rate_tax_sales = 0.06
subtotal = 0

#we include the amounts that the user entered.
print("\nPlease First enter the price and quantity for each item. ")
print("When finishing the desired prices and quantities press (0)")

price = 1
# We include the loop to save the data and the conditions.
while price !=0:
    price = float(input(("\nPlease enter the price: ")))
    if price != 0:
      quantity = int(input("please enter the quantity: "))
      subtotal += price * quantity

subtotal = round(subtotal, 2)
print(f"\nSubtotal: {subtotal:.2f}")

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system. 
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()

# we include another loop to insert the days of the discount.
if day_of_week == 1 or day_of_week == 2:
    if subtotal < 50:
        scarce = 50 - subtotal
        print("\nTo receive the discount, add"
                f" {scarce:.2f} to your order.")
    else:
        discount = round(subtotal * rate_discount, 2)
        print(f"Discount amount: {discount:.2f}")
        subtotal -= discount

# we include the final output values
sales_tax = round(subtotal * rate_tax_sales, 2)
print(f"Sales tax amount: {sales_tax:.2f}")

total = subtotal + sales_tax

print(f"Total to pay: {total:.2f}")
print("\n Thanks for participating.")