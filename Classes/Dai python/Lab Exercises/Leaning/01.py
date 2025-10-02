
# Input the five-digit number
number = int(input("Enter a five-digit number: "))

# Extract each digit using modulus (%) and integer division (//)
digit1 = number // 10000
digit2 = (number // 1000) % 10
digit3 = (number // 100) % 10
digit4 = (number // 10) % 10
digit5 = number % 10

# Calculate the sum of digits
sum_of_digits = digit1 + digit2 + digit3 + digit4 + digit5

# Print the result
print("The sum of the digits is:", sum_of_digits)

# Q17: a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. ✅
# Sample String : 'restart'
# Expected Result : 'resta$t'

string = "resultrerere"

first_char = string[0]

result = first_char + string[1:].replace(first_char,"7")
    
print(result)







# Input two strings
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Swap the first two characters of each string
new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]

# Combine them with a space
result = new_str1 + " " + new_str2

# Print the result
print("Expected Result:", result)





# [Based on Python Data Types (String, List & Conditional statements]
# Q1: Write a Python program to sum all the items in a list.

list1 = [1,23,4,5,4,5,66]

print(sum(list1))




# Q2: Write a Python program to get the largest number from a list.

# for largest number from a list we will be using the control statements 


list1 = [1,23,4,5,4555,5,66]


max = 0
for i in list1:
    if i > max:
        max = i
    else:
        pass

print(max)




# Q3: Write a Python program to get the smallest number from a list. ✅


list1 = [23,4,5,4555,5,66]

min = 10000000000000
for i in list1:
    if i < min:
        min = i
    else:
        pass

print(min)


# Q4: Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]

print(color_list[1],color_list[-1])


# Q8: Write a Python program to check if the input year is a leap year or not.


# Q9: write a Program to check if a string is palindrome or not

