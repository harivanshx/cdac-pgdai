nums = [1,2,3,4,5,]

# print(next(nums))

i_nums = iter(nums)

# also you can write 
# i_nums = nums.__iter__()

print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))


print(dir(i_nums))


  