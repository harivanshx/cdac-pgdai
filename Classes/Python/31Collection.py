# a collenction is a single variable which can store multiple values

#listwe will user square brackets ordered and changeable . Duplicates okay  [apple ,banana , coconut]

# fruits = ["apple","mango","banana","orange","grapes"]


# for fruit in fruits:
#     print(fruit)

# # print(fruits[5])
# # print(dir(fruits))
# # print(help(fruits))
# print(len(fruits))
# print("apple" in (fruits))
# fruits[0] = "pineapple"
# print("pineapple" in (fruits))
# fruits.append("apple")
# fruits.pop()
# fruits.remove("banana")
# fruits.insert(0,"banana")
# fruits.sort()
# fruits.reverse()
# print(fruits.index("grapes"))

# print(f"count of banda{fruits.count("banda")}")
# for fruit in fruits:
#     print(fruit)



##sets 

# a set is a collection of data in which only distinct objects , unordered and immutable , you ccan add or delete elements 

stationary = {"book","notebook","pencil","ereaser","sharpner"}

print(len(stationary))
stationary.add("scale")
print(stationary)
stationary.pop()
print(stationary)




# tupples are ordered and unchangable duplicates are olkay . They re faster than lists
fruits =("apple","mango " ,"banana", "orange","grapes")
print(len(fruits))
print(fruits)
print(fruits[1])
print(fruits.count("banana"))
for fruit in fruits:
    print(fruit)