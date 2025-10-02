numpad = ((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))

for collection in numpad:
    for number in collection:
        print(number,end=" ")
    print()