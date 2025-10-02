item = input("What item would you like to buy: ")
price = float(input("What is the price? "))
qty = int(input("How many do you want? "))


total = price*qty

print(f"You bought {qty} of {item} and the toatl cost is {total}")