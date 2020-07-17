#TypeError: unsupported operand type(s) for +: 'Vector2D' and 'Vector2D'
class Vector2D():
    def __init__(self,x,y):
        self.x = x
        self.y = y



v1 = Vector2D(1,2)
v2 = Vector2D(3,4)
v3 = v1+v2 #생성자만 만든다고 해서 그 값을 더할 수 있는 것이 아니다.