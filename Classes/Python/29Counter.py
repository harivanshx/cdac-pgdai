import time 
 


def count(start,end = 10):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Done")


count(5,65)




# keyword argument 
# a keyword argument preceded by an identifier helps with readibility
# order of arguments doesnot matter
# 1. Positional
# 2. Default
# 3. Keyword 
# 4. Arbutarary




