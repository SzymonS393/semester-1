"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Szymon Sihota
"""
import math

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
try:
  saveAmount = int(input("Enter the amount you would like to save every month as an integer: "))
except:
  print("Invalid amount.")


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
total = saveAmount * 12
print("You will have saved", total, "by the end of the year")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).
total += total * 0.008
total = math.floor(total * 100)/100

print("£" + str(total) + "0")

