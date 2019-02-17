## Class and Attributes

## 1) Define a class !!!
## 2) Create a class with attributes !!!
## 3) Create a class Object attribute !!!
## 1) Define a class !!!

class simple():
    pass

my_class = simple() # Object

type(my_class)

## 2) Create a class with attributes !!!

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
P1 = Person("John", 27)
type(P1)

P1.name
P1.age

## 3) Create a class Object attribute !!!

class Person():
    
    eyes = "Blue" # class Object attribute
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
P1 = Person("John", 28)
P1.eyes

P1.eyes = "Red"
