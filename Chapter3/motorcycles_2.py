#! /usr/bin/env python3

motorcycles = ['honda','yamaha','suzuka']
last_owned = motorcycles.pop()
print(motorcycles)
print("The last motorcycle I owned was a " + last_owned.title() + ".")

print("--------")
first_owned = motorcycles.pop(0)
print("The first motorcycle I onwed was a " + first_owned.title() + '.')
print(motorcycles)

print("--------")
