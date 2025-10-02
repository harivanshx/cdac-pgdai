

def greet(fx):
    def mfx(*args,**kwargs):
        print("Hello Boss")
        fx(*args,**kwargs)
        print("What you want to do today ??")
    return mfx

@greet
def yo():
    print("Its very nice to meet you again ")



@greet
def add(a,b):
    print(a+b)




add(4,5)
yo()