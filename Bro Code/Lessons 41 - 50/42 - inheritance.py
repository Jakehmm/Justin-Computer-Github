# Parent class

class Animal:

    alive = True

    def eat(self):
        print("This animal is eatingg!")

    def sleep(self):
        print("This animal is sleeping!")


class Rabbit(Animal):

    def run(self):
        print("This rabbit is running")

class Hawk(Animal):

    def flying(self):
        print("This Hawk is flying!")

class Fish(Animal):

    def swim(self):
        print("This fish is swimming!")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()


rabbit.run()
fish.swim()
hawk.flying()