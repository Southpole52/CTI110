#Anthony Love
#04/14/2024
#P2Lab2
#Building a dictionary

cars = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}

cars_keys = cars.keys()

print(cars_keys)


print(*cars_keys, sep = ", ")

car_name = input("Enter a vehicle to see it's mpg: ")
car_mpg = cars[car_name]

print()

print(f"The {car_name} gets {car_mpg} miles per gallon")

print()

miles = float(input(f"How many miles will you drive the {car_name}?"))

print

gallons = miles/car_mpg

print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {car_name} {miles} miles.")
