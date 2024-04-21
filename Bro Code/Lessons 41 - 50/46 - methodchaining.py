# Method chaining = calling multiple methods sequentially 
# Each call performs an action on the same object and 
# returns self 

# To use method chaining, we have to use "self"

class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self
    
    def brake(self):
        print("You stepped on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()

# ------- How we normally do it

# car.turn_on
# car.turn_off

# ---- Method chaining

# car.turn_on().drive()
# car.brake().turn_off


# ---- Everything in one

car.turn_on()\
.drive()\
.brake()\
.turn_off()