class BankAccount:
    def __init__(self, name, number, acc_type, balance=0):
        self.name = name
        self.number = number
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"The amount of Rs. {amount} has been deposited successfully.")
        else:
            print("❌ Invalid Amount.")

    def withdrawal(self, amount):
        if amount > self.balance:
            print("❌ Insufficient balance in your account.")
        else:
            self.balance -= amount
            print(f"The amount of Rs. {amount} has been deducted from your {self.acc_type} account.")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Account Number: {self.number}")
        print(f"Account Type: {self.acc_type}")
        print(f"Balance: Rs. {self.balance}")

    @staticmethod
    def new_customer():
        name = input("Enter Name of Depositor: ")
        number = input("Enter Account Number: ")
        acc_type = input("Enter Type of Account (Savings/Current): ")
        balance = float(input("Enter Initial Balance: "))
        return BankAccount(name, number, acc_type, balance)


account = None  

while True:
    print("\n===== Bank Menu =====")
    print("1. New Customer")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        account = BankAccount.new_customer()
        print("✅ New customer created successfully.")

    elif choice == "2":
        if account:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        else:
            print("⚠️ Please create an account first.")

    elif choice == "3":
        if account:
            amount = float(input("Enter amount to withdraw: "))
            account.withdrawal(amount)
        else:
            print("⚠️ Please create an account first.")

    elif choice == "4":
        if account:
            account.display()
        else:
            print("⚠️ Please create an account first.")

    elif choice == "5":
        print("👋 Thank you for banking with us!")
        break

    else:
        print("❌ Invalid choice. Please try again.")




# 2. Write program to create a base class staff with code and name. Derive classes
# teacher(subject , publication) , typist (speed) , officer (grade) . Using the typist class as
# base class,create two classes regular(salary) and casual(daily wages).Implement a
# menu driven program for the same.

# Output:
# 1. Teacher
# 2. Officer,
# 3. Regular Typist
# 4. Casaul typist
# 5. Exit



class staff:
    def __init__(self,code,name):
        self.c=code
        self.n = name
    def display(self):
        print(f"Code: {self.code}, Name: {self.name}")


class teacher(staff):
    def __init__(self,code,name,subject,publication):
        super().__init__(code,name)
        self.subject = subject
        self.publication = publication

    def display(self):
        print(f"Subject: {self.subject}, Publications {self.publication}")



class typist(staff):
    def __init__ (self,code,name,speed,):
        super().__init__(code,name)
        self.speed = speed

    def display(self):
        print(f"Speed:  {self.speed}")
        



class officer(staff):
    def __init__ (self,code,name,grade):
        super().__init__(code,name)
        self.grade =grade

    def display(self):
        print(f"Officer Grade = :  {self.grade}")
        
class regular(typist):
    def __init__ (self,code,name,speed,salary):
        super().__init__(code,name,speed)
        

        self.salary = salary
    def display(self):
        print(f"Regular salary:  {self.salary}")
class casual(typist):
    def __init__ (self,code,name,speed,daily_wages):
        super().__init__(code,name,speed)

        self.daily_wages = daily_wages
    def display(self):
        print(f"Daily Wage salary:  {self.daily_wages}")










