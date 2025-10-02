a= 30      
# variables = container to store a value. 
b= "harry" # keywords = reserved words in python  
c= 71.22   # identifiers = class/function/variable name 

print(a)
print(b)
print(c)



# Primarily these are the following data types in Python: 
# 1. Integers 
# 2. Floating point numbers 
# 3. Strings 
# 4. Booleans  
# 5. None 
# Python is a fantastic language that automatically identifies the type of data for us. 
# a= 71         
# # identifies a as class <int> 
# b=88.44       
# # identifies b as class <float> 
# name= "harry" # identifies name as class <str>

# RULES FOR CHOOSING AN IDENTIFIER 
# • A variable name can contain alphabets, digits, and underscores. 
# • A variable name can only start with an alphabet and underscores. 
# • A variable name can’t start with a digit. 
# • No while space is allowed to be used inside a variable name.



# Examples of a few variable names are: harry, one8, seven, _seven etc.


# OPERATORS IN PYTHON 
# Following are some common operators in python: 
# 1. Arithmetic operators: +, -, *, / etc. 
# 2. Assignment operators:  =, +=, -= etc. 
# 3. Comparison operators: ==, >, >=, <,  != etc. 
# 4. Logical operators: and, or, not.


# TYPE() FUNCTION AND TYPECASTING.  
# type() function is used to find the data type of a given variable in python. 
# a = 31  
# type(a) # class <int> 
# b = "31" 
# type (b) # class <str> 
# A number can be converted into a string and vice versa (if possible) 
# There are many functions to convert one data type into another. 
# str(31)    
# =>"31"   # integer to string conversion 
# int("32")  => 32    
# # string to integer conversion 
# float(32)  => 32.0  # integer to float conversion 
# … and so, on 
# Here "31" is a string literal and 31 a numeric literal. 
# INPUT () FUNCTION 
# This function allows the user to take input from the keyboard as a string. 
# A = input ("enter name")   # if a is "harry", the user entered harry 
# It is important to note that the output of input is always a string (even is a number is 
# entered).




# 1. Write a python program to add two numbers. 
# 2. Write a python program to find remainder when a number is divided by z. 
# 3. Check the type of variable assigned using input () function. 
# 4. Use comparison operator to find out whether ‘a’ given variable a is greater than 
# ‘b’ or not. Take a = 34 and b = 80 
# 5. Write a python program to find an average of two numbers entered by the user. 
# 6. Write a python program to calculate the square of a number entered by the user.



a = 55
b =44
c = a+b
print(c)



z = 44
x = 99

print(x%z)
