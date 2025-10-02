

def countDown(num):
    while num>0:
        yield num

print(countDown(55))
