n_list = [1,20,-3,4,-20,10,100]

minus_list = lambda x: x<0
list_m = []

for a in filter(minus_list,n_list):
    print(a)
    list_m.append(a)    

print(list_m)