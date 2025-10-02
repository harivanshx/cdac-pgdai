# Lab Exercise-6
# 1: Subtract a week ( 7 days)  from a given date in Python

from datetime import datetime, timedelta

def subtract_week(date_str, format="%Y-%m-%d"):

    date_object = datetime.strptime(date_str, format)
    new_date = date_object - timedelta(days=7)
    return new_date.strftime("%Y-%m-%d") # Format back to string
  
date_to_subtract = "2023-10-26"
print(subtract_week(date_to_subtract))




# 2: Add week ( 7 days) and 12 hours to a given date




def addweekAnd12hours(date_str, format="%Y-%m-%d"):

    date_object = datetime.strptime(date_str, format)
    new_date = date_object + timedelta(hours=12)
    return new_date.strftime("%Y-%m-%d-%h-%m") # Format back to string
  
date_to_add = "2023-10-26"
print(addweekAnd12hours(date_to_add))








# 4: Calculate number of days between two given dates
# Given:
# # 2020-02-25
# date_1 = datetime(2020, 2, 25)
# # 2020-09-17
# date_2 = datetime(2020, 9, 17)
# Expected output:
# 205 days
# 

date_1 = datetime(2020, 2, 25)
date_2 = datetime(2020, 9, 17)






# 5:  Write a Python script to display the 
# a) Current date and time
# b) Current year in full
# c) Month of year full name
# d) Weekday of the week
# e) Day of the month
# f) Day of week in full name



import datetime


now = datetime.datetime.now()

print(datetime.datetime.now())
print(now.year)
print(now.strftime("%B"))
print(now.strftime("%A"))
print(now.day)
print(now.strftime("%A"))







# 6: Follow the steps:
# •	Create a class, Triangle. Its __init__() method should take self, angle1, angle2, and angle3 as arguments. Make sure to set these appropriately in the body of the __init__()method.
# •	Create a variable named number_of_sides and set it equal to 3.
# •	Create a method named check_angles. The sum of a triangle's three angles is It should return True if the sum of self.angle1, self.angle2, and self.angle3 is equal 180, and False otherwise.
# •	Create a variable named my_triangle and set it equal to a new instance of your Triangle class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).
# •	Print out my_triangle.number_of_sides and print out my_triangle.check_angles().






