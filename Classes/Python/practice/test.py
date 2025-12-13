print("abc" * 2)
print(bool([]))
a = [1,2]
b = a * 2
print(b)


print(type(range(5)))

for i in range(3):
    print(i)
else:
    print("done")


restult = list(map(lambda x: x*x, [1,2,3]))
print(restult)


d = {1:'a', 2:'b'}
print(d.get(1, "x"))


a = [1,2]
b = a * 2
print(b)


print("abc" * 2)




a = {1,2,3}
b = {3,4,5}
print(a & b)


x = "hello"
print(x[1:4])


print(type(lambda x: x+1))



# 20. Which keyword is used for exceptions?

# A) final
# B) except
# C) catch
# D) error



class A:
    pass
a = A()
print(isinstance(a, A))
