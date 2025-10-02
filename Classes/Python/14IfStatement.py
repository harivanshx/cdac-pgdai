age = int(input("enter your age: "))
if age>=20 and age<=40:
    print("you can Drive")
elif age>40 and age<60:
    print("Bruh you are old")
else:
    print("who are you????")


response = input("would you like to have some food")
if response == "y":
    print("HAve some food bro")
else:
    print("No food for you ")


name = input("Enter your name ")
if name == "":
    print("You didnt enter your name ")
else: print(f"Hello Mr {name}")