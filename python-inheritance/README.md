Python - Inheritance
Inheritance is a powerful object-oriented programming concept that allows one class to inherit properties and methods from another class. It promotes code reuse and helps to create a hierarchy of classes, where a child class (subclass) inherits attributes and behaviors from a parent class (superclass).

Table of Contents
Introduction to Inheritance
Defining Subclasses
Overriding Methods
Super() Function
Multiple Inheritance
Method Resolution Order (MRO)
Inheritance and Constructors
Abstract Base Classes (ABCs)
Final Thoughts
Introduction to Inheritance
Inheritance allows us to create a new class that inherits attributes and behaviors (methods) from an existing class. The existing class is called the parent class or superclass, and the new class is called the child class or subclass.

For example, if we have a Vehicle class with properties and methods related to vehicles in general, we can create subclasses like Car, Bicycle, and Motorcycle that inherit from the Vehicle class and add their specific properties and methods.

Defining Subclasses
To define a subclass, use the following syntax:

python
Copy code
class ChildClassName(ParentClassName):
    # Subclass attributes and methods
For instance, if we have a Vehicle class and want to create a Car subclass:

python
Copy code
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
Overriding Methods
Subclasses can override (redefine) methods inherited from the parent class. This allows the subclass to provide its own implementation while inheriting other aspects from the parent class.

python
Copy code
class Vehicle:
    def make_sound(self):
        print("Vroom!")

class Car(Vehicle):
    def make_sound(self):
        print("Honk honk!")
Super() Function
The super() function allows access to the methods and attributes of the parent class within the child class.

python
Copy code
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
Multiple Inheritance
Python supports multiple inheritance, where a subclass can inherit from multiple parent classes. Be cautious with multiple inheritance to avoid complications.

class ElectricCar(Car, ElectricVehicle):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        ElectricVehicle.__init__(self, battery_capacity)
Method Resolution Order (MRO)
Python uses the C3 Linearization algorithm to determine the order in which methods are inherited from parent classes in cases of multiple inheritance.

Inheritance and Constructors
When defining constructors in subclasses, it's important to call the constructor of the parent class using super().__init__() to ensure the proper initialization.

Abstract Base Classes (ABCs)
Abstract Base Classes provide a way to define abstract methods in a base class, which must be implemented by subclasses. This enforces a specific interface for subclasses.

Final Thoughts
Inheritance is a fundamental concept in object-oriented programming that allows for code reuse and creating more specialized classes from existing ones. It enables the construction of complex class hierarchies and promotes a more organized and maintainable codebase.
