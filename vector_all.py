class Vector2D:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):      #문자열을 출력하려고 사용
        return '({} , {})'.format(self.x,self.y)

    def add(self , other):
        return Vector2D(self.x + other.x , self.y + other.y)

    def __add__(self , other):  #특수 메소드라고함
        return Vector2D(self.x + other.x , self.y + other.y)

    def eq(self , other):
        Vector2D(self.x==other.x,self.y==other.y)

    def __eq__(self,other): # 비교를 가능하게(같으면 true) 하는 내부 메소드
        Vector2D(self.x==other.x,self.y==other.y)

        if(self.x==other.x,self.y==other.y):
            return '같습니다'
        else:
            return '다릅니다'

    def __mod__(self,other): # 나머지를 가능하게 하는 내부 메소드
        return Vector2D(self.x%other.x,self.y%other.y)

    def sub(self , other):
        return Vector2D(self.x-other.x,self.y-other.y)

    def __sub__(self,other): # 빼기를 가능하게 하는 내부 메소드
        return Vector2D(self.x-other.x,self.y-other.y)
        
    def __del__(self): # 종결자 메소드
        print("This process is End")