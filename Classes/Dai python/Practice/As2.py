# Lab Exercise - 2

# [Based on Python Data Types (String, List &amp; Conditional statements]
# Q1: Write a Python program to sum all the items in a list.

a = [1,2,3,4,5,6,7,8,9]

x= sum(a)
print(x)




# Q2: Write a Python program to get the largest number from a list.


a = [1,2,3,4,5,55,6,7,8,9]
max = 0
for i in a:
    if i>max:
        max = i
    

print(max)




# Q3: Write a Python program to get the smallest number from a list.


a = [55,2,3,4,5,55,6,7,8,9]
min = a[0]
for i in a:
    if i<min:
        min = i
    

print(min)




# Q4: Write a Python program to display the first and last colors from the following list.
# color_list = [&quot;Red&quot;,&quot;Green&quot;,&quot;White&quot; ,&quot;Black&quot;]



color = ["red","blue","green","Purple","orange"]

first_and_last = color[0], color[-1]
print(first_and_last)

# Q5: Write a Python program to add &#39;ing&#39; at the end of a given string (length should be at least 3).
# If the given string is already ends with &#39;ing&#39; then add &#39;ly&#39; instead.




# Q6: The marks obtained by a student in 5 different Subjects are input through a keyboard. The
# Student gets a division as per the following rules.
# 1. Percentage above or equal to 60 – First Division
# 2. Percentage between 50 and 59 – Second Division
# 3. Percentage between 40 and 49 – Third Division
# 4. Percentage less than 40 – Fail



marks = []

for i in range(5):
    inp = int(input(f"Enter the marks for the subject no : {i}"))
    marks.append(inp)

print(marks)
percentage = sum(marks)/5

if percentage >= 60:
    print("You Got FIrst division")
elif percentage >=50 and percentage <=59:
    print("You got second division ")
elif percentage >=40 and percentage <=49:
    print("You got third division ")
    
elif  percentage <=40:
    print("You got faild division ")
    





# Write a python program to Display the result based on the above Criteria.
# Q7: write a Python program to find the largest number among the three input numbers
one,two,three =  int(input()),int(input()),int(input())
if(one>two):
    if(one>three):
        print("One is largest")
    else:
        print("Three is largest")
elif two>one:
    if(two>three):
        print("Two is largest")
    else:
        print("Three is largest")
    

# Q8: Write a Python program to check if the input year is a leap year or not.

# leap =  
# A year is a leap year if:

# It is divisible by 4.

# But if it is divisible by 100, then it is not a leap year.

# However, if it is divisible by 400, then it is a leap year.

# Examples:

# ✅ 2020 → Leap year (divisible by 4, not by 100)

# ❌ 1900 → Not a leap year (divisible by 100 but not by 400)

# ✅ 2000 → Leap year (divisible by 400)

# ❌ 2023 → Not a leap year


year = int(input())
leap = False
if year % 4 == 0:

    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
        else:
            leap = False

    else:
        print(True)


print(leap)


# Q9: write a Program to check if a string is palindrome or not


# string = "harirah"
# reverse = string[::-1]

# for i in string:
#     if string[i] == reverse[i]:
#         print("Yes a palendrome")
     
#     else:
#         print("Not a palendrome")

string = "hairah"
reverse = string[::-1]

is_palindrome = True
for i in range(len(string)):
    if string[i] != reverse[i]:
        is_palindrome = False
        break

if is_palindrome:
    print("Yes, it is a palindrome")
else:
    print("Not a palindrome")






# Q10: Given a nested list. Write a python program to extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like the following list
# Given List:
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# Sub List to be added = ["h", "i", "j"]
# Expected output:
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n]


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]


subl = ["h", "i", "j"]

list1[2][1][2].extend(subl)
print(list1)



# Q11: Write a python program for Given a Python list, to find value 20 in the list, and if it is
# present, replace it with 200. Only update the first occurrence of a value
# list1 = [5, 10, 15, 20, 25, 50, 20]
# Expected output:
# list1 = [5, 10, 15, 200, 25, 50, 20]

list1 = [5, 10, 15, 20, 25, 50, 20]

if 20 in list1:
    index = list1.index(20)
    list1[index] = 200

print(list1)

# Q12: Write a program to rotate a list to the right by k steps.

# Example: [1,2,3,4,5], k=2 → [4,5,1,2,3].


# list2 = [1,2,3,4,5]
# templist = []
# for i in range (len(list2)):
#     templist[i] = list2[i-2]
# print(templist)



list1=[1,2,3,4,5]
k=3
x = list1[-(k) : ] + list1[  : -(k)]

print(x)