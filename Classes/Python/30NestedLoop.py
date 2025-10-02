# a loop inside a loop is called nested loop

for x in range(0,5):
    for y in range(0,x):
        print("*",end="")
    
    print()



rows = int(input("Enter the number of rows : "))
col =  int(input("Enter the number of cols : "))
symbol = input("Enter the  symbol : ")

for x in range(rows):
    for y in range(col):
        print(symbol,end="")
    
    print()
