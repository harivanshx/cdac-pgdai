#write a program to add all the odd numbers from 0 to 20
sum = 0
for i in range (21):
    if i%2!=0:
        sum = sum + i
        
print(sum)
        
    

# write a python to find the sum of all integers greater than 100 and less than 200
sum = 0
for i in range (100,200):
    sum = sum + i 
print(sum)


#write a program to display the sum of square of the first ten even natural numbers
sum = 0
for i in range(10):
     if i%2!=0:
  
        sum = i**2+sum
print(sum)



# Q4|: Write a menu driven program to perform various list operations, such as:
# 1. Append an element
# 2. Insert an element at the desired position
# 3. Append a list to the given list
# 4. Modify an existing element
# 5. Delete an existing element by its position
# 6. Delete an existing element by its value
# 7. Sort the list in ascending order
# 8. Sort the list in descending order
# 9. Display the list
# 10.Exit

list1 = ["apple",24,44,35,"CDAC","Noida"]
# menu driven program 


# op= input("Enter a keyword to perform operation a,i,al,me,dep,dev,sort,sortd,disp,exit")
# if op == "a":
#     a = input("Enter a value you want to append to the list : ")
#     list1.append(a)
# elif op == "i":
#     a = input("Enter a value you want to insert to the list : ")
#     list1.insert(a)

# elif op == "al":
#     a = input("Enter a LIST you want to insert to the list : ")
#     list1.insert(a)
# elif op == "me":
#     a = input("Enter an element you want to change to the list : ")
#     list1()
# elif op == "dep":
#     a = input("Enter an element you want to change to the list : ")
#     list1()
# elif op == "dev":
#     a = input("Enter an element you want to change to the list : ")
#     list1()
# elif op == "sort":
#     a = input("Enter an element you want to change to the list : ")
#     list1()
# elif op == "sortd":
#     a = input("Enter an element you want to change to the list : ")
#     list1()
# elif op == "disp":
#     a = input("Enter an element you want to change to the list : ")
#     list1()
# elif op == "exit":
#     a = input("Enter an element you want to change to the list : ")
#     list1()



def menu():
    print("\n------ List Operations Menu ------")
    print("1. Append an element")
    print("2. Insert an element at the desired position")
    print("3. Append a list to the given list")
    print("4. Modify an existing element")
    print("5. Delete an element by its position")
    print("6. Delete an element by its value")
    print("7. Sort the list in ascending order")
    print("8. Sort the list in descending order")
    print("9. Display the list")
    print("10. Exit")

# Main Program
my_list = []

while True:
    menu()
    choice = int(input("Enter your choice (1-10): "))

    if choice == 1:
        element = input("Enter element to append: ")
        my_list.append(element)

    elif choice == 2:
        element = input("Enter element to insert: ")
        pos = int(input("Enter position (index): "))
        if 0 <= pos <= len(my_list):
            my_list.insert(pos, element)
        else:
            print("Invalid position!")

    elif choice == 3:
        new_list = input("Enter list elements separated by space: ").split()
        my_list.extend(new_list)

    elif choice == 4:
        pos = int(input("Enter index to modify: "))
        if 0 <= pos < len(my_list):
            new_val = input("Enter new value: ")
            my_list[pos] = new_val
        else:
            print("Invalid index!")

    elif choice == 5:
        pos = int(input("Enter index to delete: "))
        if 0 <= pos < len(my_list):
            removed = my_list.pop(pos)
            print(f"Removed element: {removed}")
        else:
            print("Invalid index!")

    elif choice == 6:
        val = input("Enter value to delete: ")
        if val in my_list:
            my_list.remove(val)
            print(f"Removed element: {val}")
        else:
            print("Value not found!")

    elif choice == 7:
        my_list.sort()
        print("List sorted in ascending order.")

    elif choice == 8:
        my_list.sort(reverse=True)
        print("List sorted in descending order.")

    elif choice == 9:
        print("Current List:", my_list)

    elif choice == 10:
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please select between 1-10.")


# Q4: Write a python program to display ascii characters from 65 to 90

for i in range (65,90):
    print(i,":",chr(i))


for i in range (48,58):
    print(i,":",chr(i))


for i in range (97,123):
    print(i,":",chr(i))


list2 =[100,200,300,400,500]
list2.reverse()
print(list2)


# Q8: Given a Python list. Write a python program to turn every item of a list into its square List1 = [1, 2, 3, 4, 5, 6, 7]

# Expected output:

# [1, 4, 9, 16, 25, 36, 49]


list2 = [1, 2, 3, 4, 5, 6, 7]
for x in range(len(list2)):
    list2[x]=list2[x]**2
print(list2)










# # Q9: Program to count the number of each vowel in a string.
# string = "HarivanshBhardwaj"
# a,e,i,o,u = 0,0,0,0,0
# n=len(string)
# for i in range(n):
#     if "a" in string:
#         a=a+1
#     elif "e" in string:
#         e=e+1
#     elif "i" in string:
#         i=i+1
#     elif "o" in string:
#         o=o+1
#     elif "u" in string:
#         u=u+1

# print(f'''the number of a in the given string is : {a} 
#         the number of e in string is {e}
# the number of  i in string is {i}
# the number of  o in string is {o}
# the number of u in string is {u}''')
        
string = "HarivanshBhardwaj"
string = string.lower()
vowal_count = {"a":0,"e":0,"i":0,"o":0,"u":0}

for char in string :
    if char in vowal_count:
        vowal_count[char]+=1

print(vowal_count)



# Q10: write a Program to sort alphabetically the words form a string provided by the user. 
# [You can use split() method to split string into a list of words. ]



string = input("Enter a string please")


list1 = string.split("_")

list1.sort()

newstring = str(list1)

print(newstring)

print(type(newstring))





# Q 11: write a Program to Remove Punctuations from a String provided by the user. 
# [Hint: use punctuation attribute of string module to get all punctuations (i.e. !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ) ]

import string
stringd = input("Enter a string value : ")
result=""
for s in stringd:
    if s not in string.punctuation:
        result+=char
    

print(result)


# Q12: Write a python program to print the Following:


# 1
# 21
# 321


for i in range (1,4):
    for j in range (i,0,-1):
        print(j,end=" ")

    print()




# Q13: Write a python program to print the Following:


# *
# **
# ***
# ****
# *****

for i in range (5):
    for j in range (i+1):
        print("*",end=" ")
    print()


# Q14: WAP to create a function traiangle to print the following asterisk triangle pattern:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *



rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

for i in range(rows - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()




# write a python program to print the following multiplication table on the screen 
#1 to 10


for i in range (1,11):
    if(i<10):
        print(" ",end="")
    print(i,"|  ",end="\t")
    for j in range (1,11):
    
        print(i*j,end="\t")
    print()

