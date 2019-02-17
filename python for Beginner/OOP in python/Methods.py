## Methods

class Person():
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def my_function(self,number):
        print("I am {} and number is {} ".format(self.name,number))
        
P1 = Person("Maria", 28)
P1.age
P1.name

P1.my_function(100)


class Circle():
    
    pi = 3.14
    
    def __init__(self,radius):
        self.radius = radius
        self.area = self.pi * radius * radius
        
    def Circum(self):
        return 2 * self.pi * self.radius
    
P1 = Circle(10)

P1.area
P1.pi
P1.radius

P1.Circum()