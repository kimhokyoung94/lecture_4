#TypeError: unsupported operand type(s) for -: 'Vector3D' and 'Vector3D'
class Vector2D:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self): # 문자열을 출력하게 해주는 내부 메소드
        return '({}, {})'.format(self.x,self.y)

    def sub(self , other):
        return Vector2D(self.x-other.x,self.y-other.y)

    def __sub__(self,other): # 빼기를 가능하게 하는 내부 메소드
        return Vector2D(self.x-other.x,self.y-other.y)

v1 = Vector2D(10,20)
v2 = Vector2D(1,2)
v3 = v1.sub(v2)
v4 = v1-v2 # __sub__를 추가해야 오류메세지가 안뜬다
print(v3)
print(v4) # __sub__를 추가해야 오류메세지가 안뜬다
