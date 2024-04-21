class Animal:
    
    def eat(self): # Method signature
        print("This animal is eating")

class Rabbit(Animal):
    
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat() # It will use the one closer , (child class)