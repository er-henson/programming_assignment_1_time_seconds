# Programmer: Erik Henson
# Course: CS151 02T, Dr. Franceschi
# Date: 9/15/2019
# Project: Programming Assignment 1: Algorithms
# Program inputs: Number of Days, Hours, Minutes, and Seconds
# Data Out: The total number of seconds that have passed

# Program Explanation and instruction. Broken up on two lines to be more readable and a new line after it
print("\nThis program takes 4 inputs for Days, Hours, Minutes, and Seconds and calculates the total number of seconds that have passed within that time."
      "\nIf there are no units for a specific time, simply put 0.\n")

# Takes and converts the number of days into a float to account for decimal inputs
days = input("How many Days? - ")
days = float(days)

# Takes and converts the number of hours into a float
hours = input("How many Hours? - ")
hours = float(hours)

# Takes and converts the number of minutes into a float
minutes = input("How many Minutes? - ")
minutes = float(minutes)

# Takes and converts the number of seconds into a float. This value is simply added to the larger number
seconds = input("How many seconds? - ")
seconds = float(seconds)

# Calculations for the total number of seconds for each unit of time (put into other variables to prevent confusion)
daySec = days*(60*60*24)
hourSec = hours*(60*60)
minuteSec = minutes*60

# Total number of seconds added together in one line in the print statement. Prints to the second decimal place
print("%.2f" % (daySec+minuteSec+hourSec+seconds), " seconds have passed in that time!")