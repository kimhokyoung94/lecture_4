ages = lambda x : x>=19

#print(ages(20))

agess = [34,25,12,15,20,33]

for a in filter(ages,agess):
    print(a)