# Practice Set 

# 1. Write a python program to display a user entered name followed by Good 
# Afternoon using input () function. 

x = input("Enter your name : ")
print(f"Good Evening {x}")

# 2. Write a program to fill in a letter template given below with name and date. 
# letter = '''  
# Dear <|Name|>, 
# You are selected! 
# <|Date|> 
# ''' 

name = input("Enter a name: ")
date = input("Enter a date")
print(f"Dear {name}, \nYou are Selected \n{date}")



# 3. Write a program to detect double space in a string. 
string = "HEllo  My  Name  Is  Harivansh Bhardwaj"

if("  " in string):
    print("Double Space Detected")
else:
    print("NO Double Spaces")



# 4. Replace the double space from problem 3 with single spaces. 
doms =  string.replace("  "," ")
print(doms)
# 5. Write a program to format the following letter using escape sequence 
# characters. 


# Escape Sequence	Description	Example
# \'	Single quote	'It\'s Python!'
# \"	Double quote	"He said, \"Hello!\""
# \\	Backslash	"This is a backslash: \\"
# \n	Newline	"Hello\nWorld"
# \t	Horizontal tab	"Hello\tWorld"
# \r	Carriage return	"Hello\rWorld"
# \b	Backspace	"Hello\bWorld"
# \f	Form feed	"Hello\fWorld"
# \v	Vertical tab	"Hello\vWorld"
# \ooo	Octal value (e.g., \101 for 'A')	"Octal: \101"
# \xhh	Hexadecimal value (e.g., \x41)	"Hex: \x41"





# letter = "Dear Harry, this python course is nice. Thanks!"


letter = "Dear Harivansh,\nThis Python Course is nice.\nThanks"
print(letter)

print(letter.endswith("kls"))
a = "123456789110"
print(a[0:10:3])


# string functions in python 

# len function 
len("harry")



MyString = "harivansh"
print(MyString.capitalize())

print(MyString.count("a"))

print(MyString.find("van"))

replaced_string =  MyString.replace("ansh","Anshika")
print(replaced_string)




# escape sequence characters 
# The escape sequence characters starts with backslash



print(f"Good Afternoon {name}")
letter = '''Dear Harivansh
Bhardwaj How Are you doing 
This is nothing but for you and you'''

print(letter.replace("you","ji"))


'''Strings are immutable that means you 
 can not cchange them even if you want to they 
 will create a new object'''


