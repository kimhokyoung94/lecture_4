class   Cat:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def __str__(self):
        return 'Cat(name='+self.name+', color = '+self.color+')'
    
nabi = Cat('나비','검정색')
nero = Cat('네로','흰색')
print(nabi)
print(nero)
