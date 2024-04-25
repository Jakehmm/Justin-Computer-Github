class God:

    God = True

    def blessings(self):
        print("Oh petty human! You have received gods blessing!")

    def power(self):
        print("Oh petty animal! You have received gods power!")


class Human(God):

    def courage(self):
        print("You are a courageous son of a bitch!")

class Animal(God):

    def fight(self):
        print("Fight with the human now!")

class Alien(God):
    pass


human = Human()
animal = Animal()
alien = Alien()

print("\n")
human.blessings()
print("\n")
animal.power()
print("\n")
animal.fight()