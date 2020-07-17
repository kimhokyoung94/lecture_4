def add(x,y):
    return x+y

#print(add(25,32))


add_other = lambda x,y : x+y

#print(add_other(11,50))

def add_plus(x,y,z):
    result_1 = x+y
    result_2 = lambda y : y**3

    return int(result_1 , result_2)

print(add_plus(10,30,20))