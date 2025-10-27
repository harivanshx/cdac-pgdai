# class Atm:
#     def __init__(self):
#         self.pin = ""
#         self.balance =0
#         self.menu =()
#     def menu(self):
#         user_input = input("""
#                            how would you like to proceed 
#                            1. Enter 1 to create pin
#                            2 Enter 2 to deposit balance
#                            3. Enter 3 to withdraw amount
#                            4. Enter 4 to check balance
#                            5. Enter 5 to exit
#                            """)
#         if user_input =='1':
#             self.createPin()
#         elif user_input == "2":
#             print("Deposit amount")
            
#         elif user_input == "3":
#             print("Withdraw amount")
            
#         elif user_input == "4":
#             print("Check Balance")
            
#         else:
#             print("Bye Bye")
#     def createPin(self):
#         self.pin = input("Enter your pin")
#         print("Pin Set Successfully")
    
    
#     def deposit_bal(self):
#         self.deposit = input("Enter amount you want to deposit")
#         print("Pin Set Successfully")
        
        
        
        
        
        
        
class Car:
    color = "Blue"
    model= "Sports"
    def calculate_avg_speed(self,km,time):
        speed = km/time
        return speed
    




wagonr = Car()

wagonr.color = "Red"
wagonr.model ="Sports"

wagonrspeeed = wagonr.calculate_avg_speed(55,3)

print(wagonr.color)
print(wagonr.model)
print(wagonrspeeed)
