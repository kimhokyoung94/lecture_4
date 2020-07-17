# TypeError: unsupported operand type(s) for %: 'Vector3D' and 'Vector3D'
class Vector2D:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self): # 문자열을 출력하게 해주는 내부 메소드
        return '({}, {})'.format(self.x,self.y)

    def mod(self , other):
        return Vector2D(self.x%other.x,self.y%other.y)

    def __mod__(self,other): # 나머지를 가능하게 하는 내부 메소드
        return Vector2D(self.x%other.x,self.y%other.y)

v1 = Vector2D(10,20)
V2 = Vector2D(2,3)
v3 = v1.mod(V2)
print(v3)


#v4 = v1%V2 # 원래는 오류가 뜬다 __mod__를 추가해야 오류가 안뜸
#print(v4)