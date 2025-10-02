foods = []
prices = []
total = 0

while True:

    food = input("enter a food to buy or press q to quit ")
    if food.lower() == "q":
        print()

        
        break
    else:
        price = float(input(f"Input the price of {food}"))

        foods.append(food)
        prices.append(price)



print("-------------YOUR CART------------------------")
for food in foods:
    print(food,end=" ")

for price in prices:
   total = total+ price
print()
print(f"The total amount is {total}")