class Cat:
    color = 'red'
    #생성자 메소드
    def __init__(self , name , color):
        self.name = name
        self.color = color
    def meow(self,name):
        print('우리 고양이는 못생긴 {}'.format(name))
        print("길냥이 {}이는 색깔이 {}구요 자주 야옹~! 야옹~! 거려요".format(self.name, self.color))

gang_cat = Cat('미옹','컬러풀하')
jong_cat = Cat('태경','똥이')
gang_cat.meow('라온')
jong_cat.meow('호경')

#출력
#우리 고양이는 못생긴 라온
#길냥이 미옹이는 색깔이 컬러풀하구요 자주 야옹~! 야옹~! 거려요
#우리 고양이는 못생긴 호경
#길냥이 태경이는 색깔이 똥이구요 자주 야옹~! 야옹~! 거려요
