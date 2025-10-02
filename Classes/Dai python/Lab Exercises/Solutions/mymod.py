def countlines(name):
    with open(name, 'r') as file:
        count = 0
        for line in file:
            count += 1
    return count


def countchar(name):
    with open(name, 'r') as file:
        counts = 0
        for line in file:      
            counts += len(line) 
    return counts


def countboth(name):
    return countchar(name), countlines(name)


def test ():
    print("THIS IS A TEST FUNCTION ")



if __name__ == "__main__":
    test()





