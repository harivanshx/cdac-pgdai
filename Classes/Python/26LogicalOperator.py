food=  input("Enter the fav food of your choice ")
while food != "q":
    print(f"you enter your food {food}")
    food =  input("Enter the fav food of your choice ")
    
print("Byeeee")


#enter number between 1 to 10 
num = int (input("Enter a #Number between 1 and 10 "))

while num > 10 or num < 0:
    print("Please enter the number eagain plaease")
    num = int (input("Enter a #Number between 1 and 10 "))

print(f"You enter the number {num}")
