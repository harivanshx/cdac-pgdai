# Q1: Write a Python program which accept the radius of a circle from the user and compute
# the area.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

import math
radi = int(input("Enter the value of Radius: "))
area = math.pi *  radi**2
print(round(area,2))




# Q2: Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a
# program to convert this temperature into Centigrade degrees.

f = float(input("Enter the value of temp in f: "))
print(f"The value of temp in c is : {round((f-32)*(5/9),2)}")




# Q3: Write a Python Program to make a simple calculator that can add, subtract, multiply and
# divide
a= int(input("Enter the number a: "))
b= int(input("Enter the number b: "))

multiplication = a*b
subst = a-b
add = a+b
div = a/b

print(f"The addition of the following numbers a: {a} and b:{b} is {add}")
print(f"The substraction of the following numbers a: {a} and b:{b} is {subst}")       
print(f"The division of the following numbers a: {a} and b:{b} is {div}")
print(f"The multiplication of the following numbers a: {a} and b:{b} is {multiplication}")





# Q4: Write a Python Program to calculate the square root

import math
num = int(input("Enter num: "))
print(math.sqrt(num))

# Q5: Write a Python Program to Solve the quadratic equation ax**2 + bx + c = 0
# # Coeffients a, b and c are provided by the user
# [Hint: import complex math module - import cmath]




import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))


x = (b**2) - (4*a*c)

if x >= 0:
    # Two real solutions
    sol1 = (-b + math.sqrt(x)) / (2*a)
    sol2 = (-b - math.sqrt(x)) / (2*a)
    print(f"The solutions are {sol1} and {sol2}")
else:
    print("The equation has no real roots.")







# Q6: Write a Python Program to find the area of triangle
# # Three sides of the triangle a, b and c are provided by the user

a = 2
b=3
c =5

# The formula is: A = √[s(s - a)(s - b)(s - c)], where A is the area and s is the semi-perimeter, calculated as s = (a + b + c) / 2

s = (a + b + c) / 2

area_of_triangle = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"The area of the triangle is: {area_of_triangle}")


# Q7: If a five-digit number is input through the keyboard, write a program to calculate the sum
# of its digits without using any loop. (Hint: Use the modulus operator ‘%’)



digit = int(input("Enter a 5 digit number"))
x1 = digit%10
digit = digit //10

x2 = digit%10
digit = digit //10


x3 = digit%10
digit = digit// 10


x4 = digit%10
digit = digit// 10


x5 = digit%10
digit = digit// 10


print(x1)
print(x2)
print(x3)
print(x4)
print(x5)








# Q8: Write a Python program to print the following string in a specific format


print("I am writing this \t line to be a tab \n this is a new line \\ soy ")

# Q9: Write a Python program to display your details like name, age, and address in three
# different lines.

name = "Harivaansh"
age = 22
address = "Pune"


print(f"My name is {name} \nMy age is {age} \n \t i am from {address}")




# Q10.Create a string containing both a single quote and double quote


print("This is a quote\' and this is a double quote \" \" ")


# Q11.Create a triple quoted string that contains single and double quotes.



print(""" This is a quote\' ""and"" this is a double quote \" \" """)




# Q12.Create a character, then obtain its integer representation.

char = "a"
int_rep = ord(char)
print(int_rep)



# Q13.Create a single string containing 5 copies of the string &#39;abc&#39;.

strin = "Hello Harivansh"
print(strin*50)



# Q14.Use the multiplication operator to create a &quot;line&quot; of 50 dashes.

strin = "-"
print(strin*50)


# Q15.Convert a string to all upper case.

name = "harivansh bhardwaj"
name = name.upper()
print(name)


# Q16 : Write a Python program to get a string made of the first 2 and the last 2 chars from a
# given a string.

nexs = "artificialIntellegence"
print(nexs[:2]+nexs[-2:])



# Q17: a Python program to get a string from a given string where all occurrences of its first
# char have been changed to &#39;$&#39;, except the first char itself.
# Sample String : &#39;restart&#39;
# Expected Result : &#39;resta$t&#39;

examstr="restart" 
firs = examstr[0]
snew = examstr.replace(firs,"$")
examstr = firs+snew[1:]
print(examstr)



# Q18: Write a Python program to get a single string from two given strings, separated by a
# space and swap the first two characters of each string.
# Sample String : &#39;abc&#39;, &#39;xyz&#39; 
# Expected Result : &#39;xyc abz&#39;



# Input strings
str1 = "abc"
str2 = "xyz"

# Swap first two characters
new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]

# Join with space
result = new_str1 + " " + new_str2

print("Result:", result)
