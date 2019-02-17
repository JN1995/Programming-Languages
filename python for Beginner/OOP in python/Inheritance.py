## Inheritance

# 1) Base Class
# 2) Derived Class
# 3) Inherit methods from base class in derived class
# 4) Re-write a method in derived class
# 5) Create new method in derived class

# 1) Base Class 
class Sports():                       
    def __init__(self):
        print("Enjoy the game")
    def health(self):
        print("I am healthy")
    def excitement(self):
        print("I am exciting")
        
my_sport = Sports()
my_sport.excitement()
my_sport.health()

# 2) Derived Class

class Football(Sports):            
    def __init__(self):
        Sports.__init__(self)
        print("I am football")
    def health(self): # Re-write a method in derived class
        print("Playing football is good for health")
    def world_cup(self): # Create new method in derived class
        print("Every four year")
        
my_football = Football()
my_football.excitement() # Inherit methods from base class in derived class
my_football.health()
my_football.world_cup()
