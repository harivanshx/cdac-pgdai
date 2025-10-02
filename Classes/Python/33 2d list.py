fruits = ["apple","mango","banana", "orange"]
vegitables = ["potato","tomato","carrots","cabbage"]
dairy = ["milk","curd","ghee"]

groceries = [fruits,vegitables,dairy]
print(groceries)

groceries[0][1]="domomo"
print(groceries)


for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print()