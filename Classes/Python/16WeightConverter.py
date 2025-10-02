#weight cornvertor
import time

weight = float(input("Enter you weight : "))
unit = input("kilograms or pounds k/p : ")

if unit == "k"or unit =="K":
    weight = weight*2.205
    newUnit = "Pounds"
elif unit == "l"or unit =="L":
    weight = weight/2.205
    newUnit = "KGs"
else:
    print("Bhai theek unit daal le ")

weight = round(weight,2)

print(f"THe converted weight from {unit} to {newUnit} = {weight} {newUnit}")

time.sleep(5) 