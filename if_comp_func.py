n_lists = list(range(1,101))

squre_arr = [x**2 for x in n_lists if x%2 ==0 and x%3 ==0]

print(squre_arr)
