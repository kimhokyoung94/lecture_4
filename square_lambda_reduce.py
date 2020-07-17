from functools import reduce

n_lists = [10,20,30,40,50]
result = reduce(lambda x,y : x*y,n_lists)
print(result)