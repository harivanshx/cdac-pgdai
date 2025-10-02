# the process of converting a variable from one data type to another datatype is called type casting
# str,bool, int , float


name = "Harivansh"
age =23
gpa = 8.6
is_student = True

a= type(name)
b =type(age)
c = type(gpa)
d =type(is_student)



print(f"The type of name is {a}")
print(f"The type of age is {b}")
print(f"The type of gpa is {c}")
print(f"The is_Student of is_student is {d}")

age = age +10
gpa = int(gpa)
print(gpa)


age= float(gpa)
print(age)

age = str(age)
print(type(age))
print(age)

