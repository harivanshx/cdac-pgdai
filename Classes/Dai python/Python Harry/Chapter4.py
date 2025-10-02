# list and tupple in python  
""" What is list and tupple
list are mutable 
tuple are immutable 
"""


a =["Harivansh", "Yash","Daksh","Lakshay","Anant","Nitya","Aradhya","Vanu","Nanno"]

print(a[5:])

# unlike string list are mutable 
#you can give any value to the element of the list 


# List Methods

a.append("New Baby")
print(a)


l1 = [1,2,4,6,6,4,2,324,5345,624,2,5,89,0]
l1.sort()
l1.reverse()
print(l1)
l1.insert(3,696969)
print(l1)
l1.pop(9)
print(l1)
l1.pop()
print(l1)

l1.remove(2)
l1.remove(2)

print(l1)
print(type(tuple))

myTuple = (1,33,22,452,4,232,1211)
a,b,c,d,e,f,g = myTuple
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)


index3 = myTuple.index(33)
print(index3)
sliced = myTuple[1:5]
print(sliced)



# ==============================================================================
# Practice Set


# 1. Write a program to store seven fruits in a list entered by the user.
fruits = []
fruits = input("Enter 7 fruits separated by commas: ").split(",")
print(fruits)







# 2. Write a program to accept marks of 6 students and display them in a sorted
# manner.

marks = [77,87,79,98,75,84]
z =  
print(z)



# 3. Check that a tuple type cannot be changed in python.

a= (1,2,3,4,5,6)
a[2]= 55
print(a)


# 4. Write a program to sum a list with 4 numbers.


# 5. Write a program to count the number of zeros in the following tuple:
# a = (7, 0, 8, 0, 0, 9)




# ASSIGNMENT 6

# Ques 1) Subtract a week ( 7 days)  from a given date in Python
import datetime
x=datetime.datetime.now()
print("The current day is :",x)
print("The day before 7 days is: ",x-datetime.timedelta(days=7))
Output:
The current day is : 2025-09-10 21:45:54.348929
The day before 7 days is:  2025-09-03 21:45:54.348929

Ques 2) Add week ( 7 days) and 12 hours to a given date
Given:
# 2024-03-22 10:00:00
given_date = datetime(2024, 3, 22, 10, 0, 0)
import datetime
given_date=datetime.datetime(2024,3,22,10,0,0)
print("Given date is : ",given_date)
print("The date 7 days after :",given_date+datetime.timedelta(days=7,hours=12) )
Output:
Given date is :  2024-03-22 10:00:00
The date 7 days after : 2024-03-29 22:00:00

Ques 3) Print ten dates, each two a week apart, starting from today, in the form YYYY-MM-DD.
x=datetime.datetime.now()
print("TODAY'S DATE IS :",x)

for i in range(1,11):
    date=x+datetime.timedelta(days=(i*14))
    print(f"date after two weeks : {date.strftime("%Y-%m-%d")}")

Output:
TODAY'S DATE IS : 2025-09-10 21:48:30.971615
date after two weeks : 2025-09-24
date after two weeks : 2025-10-08
date after two weeks : 2025-10-22
date after two weeks : 2025-11-05
date after two weeks : 2025-11-19
date after two weeks : 2025-12-03
date after two weeks : 2025-12-17
date after two weeks : 2025-12-31
date after two weeks : 2026-01-14
date after two weeks : 2026-01-28

Ques 4) Calculate number of days between two given dates
Given:
# 2020-02-25
date_1 = datetime(2020, 2, 25)
# 2020-09-17
date_2 = datetime(2020, 9, 17)
import datetime
date_1=datetime.date(2020,2,25)
date_2=datetime.date(2020,9,17)
diff=date_2-date_1
print("number of days between the given two dates : ",diff.days,"days")
Output:
number of days between the given two dates :  205 days

Ques 5) Write a Python script to display the
a) Current date and time
b) Current year in full
c) Month of year full name
d) Weekday of the week
e) Day of the month
f) Day of week in full name
import datetime
x=datetime.datetime.now()
print("Current date and time",x)
print("Current year in full :",x.strftime("%Y"))
print("Month of year in full name:",x.strftime("%B"))
print("Weekday of the week :",x.strftime("%w"))
print("Day of the month :",x.strftime("%d"))
print("Day of week in full name :",x.strftime("%A"))
Output:
Current date and time 2025-09-10 21:50:54.708661
Current year in full : 2025
Month of year in full name: September
Weekday of the week : 3
Day of the month : 10
Day of week in full name : Wednesday

Ques 6) Follow the steps:
• Create a class, Triangle. Its __init__() method should take self, angle1, angle2, and
angle3 as arguments. Make sure to set these appropriately in the body of the
__init__()method.
• Create a variable named number_of_sides and set it equal to 3.
• Create a method named check_angles. The sum of a triangle&#39;s three angles is It should
return True if the sum of self.angle1, self.angle2, and self.angle3 is equal 180, and False
otherwise.
• Create a variable named my_triangle and set it equal to a new instance of your Triangle
class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).
• Print out my_triangle.number_of_sides and print out my_triangle.check_angles().

class Triangle:

    number_of_sides=3

    def __init__(self,angle1,angle2,angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3
    def check_angles(self):
         if(self.angle1+self.angle2+self.angle3 == 180):
             return True
         else:
             return False
my_triangle=Triangle(90,30,60)

print("The number of sides : ",my_triangle.number_of_sides)
print("Do the angles form a triangle :",my_triangle.check_angles())
Output:
The number of sides :  3
Do the angles form a triangle : True

Ques 7) Define a class called Songs, it will show the lyrics of a song. Its __init__() method should
have two arguments: self and lyrics. Lyrics is a list. Inside your class create a method called
sing_me_a_song that prints each element of lyrics on his own line. Define a varible:
happy_bday = Song([“May god bless you, “,
“Have a sunshine on you,”,
“Happy Birthday to you !”])
Call the sing_me_song method on this variable.
class Songs:
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)
happy_bday=Songs(["May god bless you,",
                  "Have a sunshine on you,",
                  "Happy Birthday to you !"])
happy_bday.sing_me_a_song()
Output:
May god bless you,
Have a sunshine on you,
Happy Birthday to you !

Ques 8) Define a class called Lunch. Its __init__() method should have two arguments:selfanf
menu.Where menu is a string. Add a method called menu_price.It will involve a ifstatement:
• if “menu 1” print “Your choice:”, menu, “Price 12.00”, if “menu 2” print “Your choice:”,
menu, “Price 13.40”, else print “Error in menu”.
To check if it works define: Paul=Lunch(“menu 1”) and call Paul.menu_price().
class lunch:
    def __init__(self,menu):
        #self.menu=
        self.menu=menu
    def menu_price(self):
        #ch=int(input("enter your choice : "))
        if(self.menu=="menu1"):
            print(f"Your choice {self.menu} : Price 12.00")
        elif(self.menu=="menu2"):
            print(f"Your choice {self.menu} : Price 13.40")
        else:
            print("Error in menu")

a=input("Enter your choice (menu1/menu2) : ")
Paul=lunch(a)
Paul.menu_price()
Output:
Enter your choice (menu1/menu2) : menu1
Your choice menu1 : Price 12.00

Ques 9) Write a Python class which has two methods get_String and print_String. get_String accept a
string from the user and print_String print the string in upper case.
class string:
    def get_string(self):
        self.name=input("Enter any string : ")
    def print_string(self):
        a=self.name.upper()
        print("entered string in uppercase : ",a)
str=string()
str.get_string()
str.print_string()
Output:
Enter any string : simran
entered string in uppercase :  SIMRAN

Ques 10) Write a program to find the area and perimeter of a rectangle using classes and objects.
class Rectangle:

    def area(self,length,breadth):  
        self.L=length  
        self.B=breadth   
        print(f"Area of rectangle with length {(length)} and breadth {(breadth)} is : {(self.L*self.B)}") 

    def perimeter(self,length,breadth):
        self.length=length
        self.breadth=breadth

        print(f"Perimeter of rectangle with length {(length)} and breadth {(breadth)} is : {(2*(self.L+self.B))}")

rect=Rectangle()

while True:
    print()
    length=int(input("Enter length of a rectangle :"))
    breadth=int(input("Enter breadth of a rectangle :"))
    print(""" 
1)Area
2)Perimeter
3)Exit
""")
    ch=int(input("Enter your choice :"))

    if(ch==1):
        rect.area(length,breadth)
      
    elif(ch==2):
        rect.perimeter(length,breadth)
    else:
        break
Output:
Enter length of a rectangle :5
Enter breadth of a rectangle :5
 
1)Area
2)Perimeter
3)Exit

Enter your choice :1
Area of rectangle with length 5 and breadth 5 is : 25

Enter length of a rectangle :5
Enter breadth of a rectangle :5
 
1)Area
2)Perimeter
3)Exit

Enter your choice :2
Perimeter of rectangle with length 5 and breadth 5 is : 20

Enter length of a rectangle :5
Enter breadth of a rectangle :5

1)Area
2)Perimeter
3)Exit

Enter your choice :3








