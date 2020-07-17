class Vector2D:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self): # 문자열을 출력하게 해주는 내부 메소드
        return '({}, {})'.format(self.x,self.y)

    def eq(self , other):
        return Vector2D(self.x==other.x,self.y==other.y)

    def __eq__(self,other): # 비교를 가능하게(같으면 true) 하는 내부 메소드
        return Vector2D(self.x==other.x,self.y==other.y)

#v1 = Vector2D(2,3)
#V2 = Vector2D(2,3)
#v3 = v1.eq(V2)
#print(v3)

#v4 = v1==V2 # 원래는 false 뜬다 __eq__를 추가해야 결과가 잘뜸
#print(v4)