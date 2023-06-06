""" Prints a list of cars, only bmw in uppercase, the rest of the car in title case """
cars = ['audi', 'subaru', 'toyota', 'bmw']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
