# # Lab Exercise 4

# # [Based on Python data types, conditional statements & Loops]

# # Q1: Write a python program to add all the odd numbers from 0 to 20.
# odd = []
# for i in range (20):
#     if i%2 == 0:
#         pass
#     else:
#         odd.append(i)
# print(odd)

# # Q 2: Write a python program to find the sum of all integers greater than 100 and less than 200.
# sum = 0
# for i in range (100,200):
#     sum = sum +i

# print(sum)


# # Q3: Write a program to display the sum of square of the first ten even natural numbers



# # Q4|: Write a menu driven program to perform various list operations, such as:
# # 1. Append an element
# # 2. Insert an element at the desired position
# # 3. Append a list to the given list
# # 4. Modify an existing element
# # 5. Delete an existing element by its position
# # 6. Delete an existing element by its value
# # 7. Sort the list in ascending order
# # 8. Sort the list in descending order
# # 9. Display the list
# # 10.Exit

# # list1.append[inp]
# # list1.insert(position, element)
# # list1.extend(list2)
# # list1[5]= "Hari"
# # del list1[position]

# # list1.remove(value)
# # sorts = list1.sort


# # sortr  = sorts[::-1]


# # print(list1)


# # list1 = []
# # for i in range (15):
# #     x = input(f"Enter element {i+1} : ")
# #     list1.append(i)
# #     if x == " ":
# #         break


# # opp = input("")
# # if opp == "append":
# #     for i in range (15):
# #         x = input(f"Enter element {i+1} : ")
# #         list1.append(i)
# #         if x == " ":
# #             break

    
# # elif opp == "insert":
# #     pos = int(input("Enter position in number"))
# #     val = input("Enter value you want to insert here in the list ")
# #     list1.insert(pos,val)


# # elif opp == "extend":

# #     val = input("Enter value you want to insert here in the list ")
# #     list1.extend(val)

# # elif opp == "modify":
# #     pos = int(input("Enter position in number"))
# #     val = int(input("Enter position in number"))

    
# #     list1[pos] = val

# # elif opp == "del":
# #     pos = int(input("Enter position in number"))
# #     del(list1[pos])

# # # del list1[position]

# # elif opp == "rem":
# #     val = int(input("Enter val in number"))
# #     list1.remove(val)

# # # list1.remove(value)


# # # sorts = list1.sort

# # elif opp == "sort":
   
# #     list1.sort()


# # elif opp == "sortr":
   
# #     x =list1.sort()
# #     list1 = x[::-1]


# # print(list1)








# list1 = []
# for i in range(15):
#     x = input(f"Enter element {i+1} (or press Enter to stop): ")
#     if x == "":
#         break
#     list1.append(x)

# opp = input("Enter operation (append, insert, extend, modify, del, rem, sort, sortr): ").lower()

# if opp == "append":
#     for i in range(15):
#         x = input(f"Enter element {i+1} (or press Enter to stop): ")
#         if x == "":
#             break
#         list1.append(x)

# elif opp == "insert":
#     pos = int(input("Enter position: "))
#     val = input("Enter value to insert: ")
#     list1.insert(pos, val)

# elif opp == "extend":
#     val = input("Enter values separated by space: ")
#     list1.extend(val.split())

# elif opp == "modify":
#     pos = int(input("Enter position to modify: "))
#     val = input("Enter new value: ")
#     list1[pos] = val

# elif opp == "del":
#     pos = int(input("Enter position to delete: "))
#     del list1[pos]

# elif opp == "rem":
#     val = input("Enter value to remove: ")
#     list1.remove(val)

# elif opp == "sort":
#     list1.sort()

# elif opp == "sortr":
#     list1.sort(reverse=True)

# print("Updated list:", list1)

















# # Output:
# # The list 'myList' has the following elements [22, 4, 16, 38, 13]
# # L I S T O P E R A T I O N S
# # 1. Append an element
# # 2. Insert an element at the desired position
# # 3. Append a list to the given list
# # 4. Modify an existing element
# # 5. Delete an existing element by its position
# # 6. Delete an existing element by its value
# # 7. Sort the list in ascending order
# # 8. Sort the list in descending order
# # 9. Display the list
# # 10. Exit
# # ENTER YOUR CHOICE (1-10): 8
# # The list has been sorted in reverse order
# # The list 'myList' has the following elements [38, 22, 16, 13, 4]


# # Q4: Write a python program to display ascii characters from 65 to 90





# for i in range(65,91):
#     print(chr(i), end = " ")




# # Q5: Display ascii characters from 48 to 57.





# for i in range(47,57):
#     print(chr(i), end = " ")














# # Q6: Display the following output with the help of Ascii character.






# # Q7: Write a python program for given a Python list you should be able to display Python list in the following order

# L1 = [100, 200, 300, 400, 500]

# k=3
# L1 = L1[::-1] + L1[:k]
 
# print(L1)
# # Expected output:


# # [500, 400, 300, 200, 100]




# # Q8: Given a Python list. Write a python program to turn every item of a list into its square List1 = [1, 2, 3, 4, 5, 6, 7]

# # Expected output:

# # [1, 4, 9, 16, 25, 36, 49]

# # Q9: Program to count the number of each vowel in a string.

# # Q10: write a Program to sort alphabetically the words form a string provided by the user. 
# # [You can use split() method to split string into a list of words. ]





# # Q 11: write a Program to Remove Punctuations from a String provided by the user. [Hint: use punctuation attribute of string module to get all punctuations (i.e. !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ) ]


# # [Nested Loops]

# # Q12: Write a python program to print the Following:


# for i in range(1,6):
#     for j in range(1,6):
#         print(i,j)
        



	

# # Q13: WAP to print the following asterisk pattern:









   
               







# # Q14: WAP to create a function traiangle to print the following asterisk triangle pattern:



















# # Q15: Write a python program to print following multiplication table on the screen

profile = {
    "name" : "harivansh",
    "age":23,
    "salary":1500000
}


popped = profile.pop("name")
print(popped)
print(profile)



# dictionary comprehension 

squares = {x: x*x for x in range(1,6)}
print(squares)


#nested dictionary


programming_language = {
    "python":{"name":"python","usecase":['ai','ml','data analytics']}
    ,"java":{"name":"java","usecase":['dsa','Enterprise apps','Game dev']}

}

print(programming_language)



for keys in programming_language.values():
    print(keys)




# python function


# function is a block of code that perform some task in the code to get the reusablity



# def doms (dino):
#     sese = dino*55
#     return sese

# print(doms(65))

# decorators and generators

def my_deco(funct):
    def wrapper():
        print("Extra code up")
        funct()
        print("Extra code Down")
    return wrapper


@my_deco
def doms():
    print("Hello")


doms()


#generator 
# vanding machine 
# generate value on demand it behave like a iterator using yeald keyword


def countDown(num):
    while num>0:
        yield num
        num-=1


for num in countDown(10):
    print(num)