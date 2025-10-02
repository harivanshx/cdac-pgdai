# by using assertion 
# asswetion works like sanity check that you can turn on or off when you are done your testing of the program in assertion an expression is tested and if the result comes up false 
# print(dir(__builtins__))

# Exception handling and assertion 
# assert expression[, Arguments]

# sys module in sys module we have one funtion exc_info() and it help us in the finding of exception info and it return a tupple with 3 values
#     1st one neme of exception 2nd one description and in the 3rd parameter we have address
# import sys

# try:
#     print(cdac)
#     print("hello");
#     print(10/0);


# except (NameError) as ex :
#     print(sys.exc_info())



# user defined exception how can we create it 
# creating your exception you need to create a class which is derived from exception 


class invalidValueError(Exception):
    def __init__(self,data):
        self.data=data
    
    def __str__
    







# finally:
#     print("LOCALHOST");
    # print(10/0)


# if there is one try block you need to define the except block veere
# you can have multiple except with excetion type 



# tilll now exception been raised automaticaly but what about if i have do decide what is exception and what should be display
# you will use raise keyword for the same things 
# we need to spacify when exception should be raised and when it should not be 


# here is a quick example for the same thing
    



try:
    a = int(input("Enter the positive calue"))
    if a<0:
        raise ValueError("You have entered negative value")
    print(a)
    
except ValueError as ex:
    print("Error : ",ex)



