class Car:

    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"This {self.make} is driving")

    def stop(self):
        print(f"This {self.model} is stopped!")

car_1 = Car("Lamborghini", "Corvette" , "2024" , "White")
car_2 = Car("BMW" , "Mustang" , "2024" , "Blue")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_1.drive()
car_2.stop()

car_2.drive()
car_2.stop()