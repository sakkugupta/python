'''class Xyz:
    def __init__(self):
        print('hello')
    def manisha(self):
        print('sakshi')

obj=Xyz()
obj.manisha()

class Abc:
    def sub(self, x,y):
        z=x-y
        print('total',z)

obj=Abc()
obj.sub(50,25)'''

class Abd:
    staticX=10
    def __init__(self,x):
        self.x1 =10
    def add (self):
        Abd.staticX+=1
        self.x1+=1
        print('static variable',Abd.staticX)
        print('instance variable',self.x1)

obj1=Abd(23)
print(obj1.x1)
obj1.add()
obj2=Abd(23)
obj2.add()





