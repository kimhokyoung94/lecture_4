class Vector2D:
    def __init__(self,x,y): #생성자 생성
        self.x = x
        self.y = y

    def __str__(self):      #문자열을 출력하려고 사용
        return '({} , {})'.format(self.x,self.y)

    def add(self , other):
        return Vector2D(self.x + other.x , self.y + other.y)

    def __add__(self , other):  #특수 메소드라고함
        return Vector2D(self.x + other.x , self.y + other.y)

v1 = Vector2D(1,2)
v2 = Vector2D(10,20)
v3 = v1.add(v2)
v4 = v1+v2 #안됨.. __add__ 추가하니까 됨
print(v3)
print(v4) #안됨.. __add__ 추가하니까 됨