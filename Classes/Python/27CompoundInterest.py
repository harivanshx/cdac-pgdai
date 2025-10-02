principle =0
rate= 0
time= 0


while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle should be positive number and it cant be zero ")
    else:
        break


while True:
    rate = float(input("Enter the rate : "))
    if rate <= 0:
        print("rate should be positive number and it cant be zero ")
    else:
        break



while True:
    time = float(input("Enter the time in years : "))
    if time <= 0:
        print("time should be positive number and it cant be zero ")
    else:
        break
print(principle)
print(rate)
print(time)



totalAmount = principle * pow((1+rate/100),time)
interest = totalAmount-principle
print(f"The interest is {interest}")