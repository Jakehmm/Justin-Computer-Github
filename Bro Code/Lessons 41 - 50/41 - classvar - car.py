from classvar import Car 


car_1 = Car("Chevy" , "Corvette", 2021 , "White")
car_2 = Car("Ford" , "Mustang" , 2022, "Black")

Car.wheels = 2 # Affect all, and unchangable

print(car_1.wheels)
print(car_2.wheels)


print(Car.wheels) # display same as the one we made