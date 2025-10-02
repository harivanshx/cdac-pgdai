#progrram for addition of two n umbers
FN=int(input("Enter First No. :"))
SN=int(input("Enter Second No. :"))
result=FN+SN
#formattting sttring output
print("Result of addition of",FN,"and",SN,"=",result)
print("Result of addition of "+str(FN)+" and "+str(SN)+" = "+str(result))
print("Result of addition of %d and %d = %d" %(FN,SN,result))
print("Result of addition of {0} and {1} = {2}".format(FN,SN,result))
print(f"Result of addition of {FN} and {SN} = {FN+SN}")

print(issubclass(list,object),isinstance(5.5,object),isinstance("Hello",object))


# 	Class p :
# 		Pass
# 	Class C1(p):
# 		Def m1(self):
# 			Print("This message is coming from c1")
# 	Class c2(p):
# 		Def m1(self):
# 			Print("This message is coming from c2")
# 	Class c12(c1,c2):
# 		Pass
		
		
# 	It will print the message of c1 as it works on left right 
# 	If we write 
# 	Class c12(c2,c1):
# 		Pass
		
# 	Even if there is a way 
	
# 	C12.__mro__
# C12.mro()


class p:
	pass
class c1:
	def m1(self):
		print("This message is coming from c1")
	pass
class c2:
	def m1(self):
		print("This message is coming from c2")

class c12(c1,c2):
	pass
    

class Polygon:
	def __init__(self,no_of_sides):
		self.n = no_of_sides
		self.side = [0 for i in range(no_of_sides)]
		
        

# from abc import ABC , abstractmethod
from abc import *

class AbstractClass1(ABC):
	@abstractmethod
	def doSomething(self):
		print()
		

		


