"""
Conditional Tests: Write a series of conditional tests.
Print a statement describing each test and your prediction 
for the results of each test. Your code
should look something like this:
"""

cars = ['subaru', 'audi', 'toyota', 'bmw']
car = 'subaru'
if car == 'subaru':
    print("Is car == 'subaru'? I predict True")
    print(car == 'subaru')

    print("\nIs car == 'audi'? I predict False")
    print(car == 'audi')

car = 'audi'
if car == 'audi':
    print("\nIs car == 'audi'? I predict True")
    print(car == 'audi')

    print("\nIs car == 'audi'? I predict false")
    print(car == 'bmw')


car = 'bmw'
if car == 'bmw':
    print("\nIs car == 'bmw'? I predict true")
    print(car == 'bmw')

    print("\nIs car == 'bmw'? I predict false")
    print(car == 'audi')
