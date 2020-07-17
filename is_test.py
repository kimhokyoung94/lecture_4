list_a = [10, 20, 30]
list_b = [10, 20, 30]

if list_a is list_b:
    print('list_a is list_b')

else:
    print('list_a is not list_b')

print('list_a 는 :',id(list_a),'이다')
print('list_b 는 :',id(list_b),'이다')

num_a ={1,2,3}
num_b ={1,2,3}


if num_a is num_b:
    print('num_a is num_b')

else:
    print('num_a is not num_b')

print('num_a 의 주소는 :',id(num_a),'이다')
print('num_b 의 주소는 :',id(num_b),'이다')


str_a ='안녕'
str_b ='안녕'


if str_a is str_b:
    print('str_a is str_b')

else:
    print('str_a is not str_b')

print('str_a 의 주소는 :',id(str_a),'이다')
print('str_b 의 주소는 :',id(str_b),'이다')