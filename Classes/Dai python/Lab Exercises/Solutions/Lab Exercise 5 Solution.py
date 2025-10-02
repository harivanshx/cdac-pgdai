
# #1. Write a Python program to read an entire text file.



# f = open("simple.txt",mode ="r")

# print(f.read())
# f.seek(0)



# # 2.   Write a program that counts lines and characters in a file. With your favorite text editor, 
# # code a Python module called mymod.py, which exports three top-level names:
# # a) A countLines(name) function that reads an input file and counts the number of lines in it 
# # b) A countChars(name) function that reads an input file and counts the number of characters in it 
# # c) A test(name) function that calls both counting functions with a given input file¬name. 
# # All three mymod functions should expect a filename string to be passed in.
# # Now, test your module interactively, using import and name qualification to fetch your exports. 

from dino.harivansh import popy

import mymod




import mymod



print(mymod.countlines("simple.txt"))

print(mymod.countchar("simple.txt"))
print(mymod.countboth("simple.txt"))


# # 3. Test your mymod module from Exercise 2 interactively, by using from to load the exports
# # directly, first by name, then using the from* variant to fetch everything.



from mymod import countboth, countchar , countlines


    

print(mymod.countlines("simple.txt"))

print(mymod.countchar("simple.txt"))
print(mymod.countboth("simple.txt"))







from mymod import *


    

print(mymod.countlines("simple.txt"))

print(mymod.countchar("simple.txt"))
print(mymod.countboth("simple.txt"))




from pacakgexd import mymod
    

print(mymod.countlines("simple.txt"))

print(mymod.countchar("simple.txt"))
print(mymod.countboth("simple.txt"))


# # 7.  Write a Python program to read first n lines of a file.

n = 5  

with open('simple.txt', 'r') as file:
    for i in range(n):
        line = file.readline()
        if not line:
            break
        print(line.strip())





# 8. Write a Python program to append text to a file and display the text.



with open('yourfile.txt', 'a') as file:
    file.write("This is the new text.\n")

with open('yourfile.txt', 'r') as file:
    content = file.read()
    print(content)






# 9. Write a Python program to read a file line by line and store it into a list.

with open('simple.txt', 'r') as file:
    lines = [line.strip() for line in file]

print(lines)








with open('simple.txt', 'r') as file:
    lines = [line.strip() for line in file]
rev_lines = lines[::-1]


print(rev_lines)












lines = ["Hello", "World", "Python is great!"]

with open('output.txt', 'w') as file:
    for line in lines:
        file.write(line + '\n')






filename = 'simple.txt'

# Initialize counters
num_chars = 0
num_words = 0
num_lines = 0

# Open and process the file
with open(filename, 'r') as file:
    for line in file:
        num_lines += 1
        num_chars += len(line)
        num_words += len(line.split())

# Print the results
print(f"Number of characters: {num_chars}")
print(f"Number of words: {num_words}")
print(f"Number of lines: {num_lines}")












# Create and open the file to write
with open("sentences.txt", "w") as file:
    while True:
        sentence = input("Enter a sentence (type 'END' to stop): ")
        if sentence == "END":
            break
        file.write(sentence + "\n") 

# Open the file to read
print("\nSentences that start with an uppercase letter:")
with open("sentences.txt", "r") as file:
    for line in file:
        line = line.strip() 
        if line and line[0].isupper():  
            print(line)









import pickle

# Step 1 - Get number of records from the user
num = int(input("Enter number of records: "))

records = []

for i in range(num):
    print(f"\nRecord {i+1}")
    item_no = int(input("Enter Item No: "))
    item_name = input("Enter Item Name: ")
    qty = int(input("Enter Quantity: "))
    price = float(input("Enter Price per item: "))

    record = {
        "Item No": item_no,
        "Item Name": item_name,
        "Qty": qty,
        "Price": price
    }
    records.append(record)

with open("items.dat", "wb") as file:
    pickle.dump(records, file)


print("\nItems in the file:")
with open("items.dat", "rb") as file:
    records = pickle.load(file)
    for record in records:
        amount = record["Qty"] * record["Price"]
        print("\nItem No:", record["Item No"])
        print("Item Name:", record["Item Name"])
        print("Quantity:", record["Qty"])
        print("Price per item:", record["Price"])
        print("Amount:", amount)

























# print("Program to read the first n lines of a file. ")
# print('\t', "-----"*5)

# fl = input("Enter the file name: ")
# n = int(input("Enter number of lines to read(n): "))

# with open(fl, 'r') as file:
#     content = file.readlines() 
#     i = 0
#     while i<n:
#         print("{:2}.". format(i+1),content[i], end='')
#         i+=1



# # when you require different version of python and you want to change the project deployment 
# # for that you can work with virtual environment and there are various ways to create virtual environment
# # if you are working with vs code the you can use virtual environment
# #for now on we will be working on anaconda``



# # we  dont want to disturb other things the you will able to install anaconda and use virtual environment for that 
# # and virtual environment gives you freedom to work in a isolation 


# #



# 1. Write a Python program to read an entire text file.

with open("simple.txt","r") as f:
    print(f.read())