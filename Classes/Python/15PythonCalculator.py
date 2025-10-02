operator = input("Enter an arithematic operator  ")

num1 =  float(input("input the num1 : "))
num2 =  float(input("input the num2 : "))


if operator=="+":
    print(f"The sum of a and b = {num1 + num2}")
elif operator == "-":
    print(f"The difference of a and b = {num1 - num2}")
elif operator == "/":
    print(f"The division  of a and b = {num1 / num2}")
elif operator == "*":
    print(f"The multiplication of a and b = {num1 * num2}")
else:
    print("Enter a correct operator")