# multi-level inheritance = when a derived (child) class inherits another derived
# (child) class

# Grandparent
class Organism:

    alive = True

# Parent
class Animal(Organism):

    def eat(self):
        print("This animal is eating")

# Child
class Dog(Animal):

    def bark(self):
        print("This dog is barking!")


dog = Dog()
print(dog.alive) # Inherited from grandparent class
dog.eat() # Inherited from parent
dog.bark() # Own function