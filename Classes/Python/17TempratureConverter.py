temp = float(input("Enter temprature: "))
unit = input("Enter a unit of temprature from (C,F,K) :")
if unit =="C" or unit=="c":
    temp = 9*temp/5 +32
    print(f"The tempratue in F is {temp} degree f")
elif unit == 'f' or unit == "F":
    temp = (temp - 32) * 5/9
    print(f"The tempratue in C is {temp} degree C")
else:
    print(f"the {unit} is invalid ")
    