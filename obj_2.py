class Cat:
    color = 'red'
    #생성자 메소드
    def __init__(self , name , color):
        self.name = name
        self.color = color
    def meow(self):
        print("우리 {}이는 색깔이 {}구요 자주 야옹~! 야옹~! 거려요".format(self.name, self.color))
raon = Cat('라온', "똥")
meon = Cat('미용', '컬러플하')
raon.meow()
print(meon.color)
meon.meow()