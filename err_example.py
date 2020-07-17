#list = []
#number = list(range(10))
# TypeError: 'list' object is not callable

try:
    a,b = input('두수를 넣으세요').split()
    result=(int(a)/int(b))
    print(result)
except:
    print('대입한 수가 정확한지 확인하세요')

print('test')