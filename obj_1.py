#obj_1.py
class Cat:		# 여기서 객체를 만들고
	#class variable or member
    color = 'red'
    #instance method
    def meow(self):
        print('야옹~ 야옹~!')


raon = Cat()	#여기서 호출을 하게 되어서 객체가 완성된다.
raon.meow()
