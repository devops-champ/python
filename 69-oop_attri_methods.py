class Dog:
    species = "mammal"
    
    def __init__(self, mybreed, name, spots):
        self.mybreed = mybreed
        self.name = name
        self.spots = spots
    
    #these are more like actions    
    def bark(self):
        return f"Woof! my name is {self.name}"
            
    
dog1 = Dog("pomarian", "jimmy", False) 
print(dog1.bark())

dog2 = Dog("husky", "kariya", True)
print(dog2.bark())


class Circle:
    
    pi = 3.14
    
    def __init__(self, radius):
        self.radius = radius
        self.area = radius * radius * Circle.pi # if you have an attribute it doesn't necessarily have to defined from the function 
        
    def circumference(self):
        return self.radius * self.pi * 2
    
my_circle = Circle(30)  

print(my_circle.area)  
            