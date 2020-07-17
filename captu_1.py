class   Cat:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return 'Cat(name='+self.__name+', color = '+self.__age+')'

    def set_age(self,age):
        if age > 0:
            self.__age = age

    def get_age(self):
        return self.__age

nabi = Cat('나비',3)
print(nabi)
nabi.set_age(4)
print(nabi)
nabi.set_age(-5)
print(nabi)