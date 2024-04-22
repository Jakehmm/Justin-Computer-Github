'''
class Car:

    color = None

class Motorcycle:

    color = None

def change_color(vehicle,color):

    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()
bike_2 = Motorcycle()
bike_3 = Motorcycle()

change_color(car_1,"red")
change_color(car_2,"green")
change_color(car_3,"white")
change_color(bike_1,"black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)

'''

class Vehicle:

    color = None
    wheels = None
    seat = None

def setup(vehicle, color, wheels, seat):

    vehicle.color = color
    vehicle.wheels = wheels
    vehicle.seat = seat

vehicle_1 = Vehicle()
vehicle_2 = Vehicle()
vehicle_3 = Vehicle()

setup(vehicle_1, "red" , "three" , 3)
setup(vehicle_2, "white" , "five" , 3)
setup(vehicle_3, "yellow" , "four" , 4)

print(vehicle_1.wheels)
print(vehicle_2.color)
print(vehicle_3.seat)