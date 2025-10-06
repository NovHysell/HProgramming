class Student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major
    
    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, Major: {self.major}"

# Create a new class with the Student class as a parent class
class UndergraduateStudent(Student): # UndergraduateStudent is a child of Student class
    #Override methods by giving them the same names as methods in the parent class
    def __init__(self, name, student_id, major, year):
        super().__init__(name, student_id, major) #super function calls the method from the parent class
        self.year = year
    
    def __str__(self):
        return super().__str__() + f", Year: {self.year}"
    
    def getName(self):
        print(self.name)

if __name__ == "__main__":
    student = Student("Alice", "U1020", "Computer Science")
    print(student)

    undergrad = UndergraduateStudent("Michael", "U1222", "Physics", "Freshman")
    print(undergrad) # Every undergrad is a student, not every student is an undergrad
    undergrad.getName()

# Inheritance is a fundamental concept in OOP that allows a class to inherit attriubtes and methods from another class
# The inheriting class is known as the child class, while the giving class is known as the parent class
# Inheritance is implemented by specifiying the parent class in parenthesis after the child class
# The super() function is commonly used to extend or modify the behavior of inherited methods.
# Child classes can override methods from the parent class to provide specific implementations.
class Flyer:
    def fly(self):
        print("I can fly")
class Swimmer:
    def swin(self):
        print("I can swim")
class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!") # Child class can inherit from multiple parent classes
# Multilevel inheritance: A class inherits from a parent class, which itself inherits from another class, forming a chain.
# class Animal; class Mammal(Animal); class Dog(Mammal);
# If something is private, it is not inherited