class Point:
    x = 10
    y = 7

p = Point()
print(p.x)
print(p.y)
p.x = 12
print(p.x)
print(Point.x)
del p.x
print(p.x)

p.z = 3
print(p.z)
#print(Point.z)
# AttributeError: type object 'Point' has no attribute 'z'

class Person:
    species = 'Human'

# Accessing class attributes
print(Person.species)

# Create an instance
man = Person()
print(man.species)

# Can also add instance attributes
man.name = 'Darth'
man.surname = 'Vader'
print(man.name, man.surname)

# Attribute shadowing is when an instance attribute has the same name as a class attribute