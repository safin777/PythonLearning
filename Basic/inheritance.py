#Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Create a Parent Class
# Any class can be a parent class, so the syntax is the same as creating any other class:
# Example

class Person:
     def __init__(self,name,age):
          self.firstname = name
          self.myAge = age


     def printName(self):
          print("My name is " + self.firstname + ", and my age is " + self.myAge)
perInfo = Person("safin", "21")
perInfo.printName();


# Create a Child Class

class Children(Person):
     pass

cl = Children("Ezan","2")
cl.printName();


# Add the __init__() Function
# So far we have created a child class that inherits the properties and methods from its parent.
# We want to add the __init__() function to the child class (instead of the pass keyword).
# Note: The __init__() function is called automatically every time the class is being used to create a new object.
# Example

class Children(Person):
        def __init__(self,name,age):
            Person.__init__(self,name,age)

cl = Children("Ezan","2")
cl.printName();


# Use the super() Function

class Children(Person):
        def __init__(self,name,age):
            super().__init__(name,age)

cl = Children("Ezan","2")
cl.printName();


# Add Properties
# Example

class Children(Person):
        def __init__(self,name,age,year):
            super().__init__(name,age)
            self.graduationyear = year

cl = Children("Ezan","2","2020")

print(cl.graduationyear)


# Add Methods
# Example

class Children(Person):
        def __init__(self,name,age,year):
            super().__init__(name,age)
            self.graduationyear = year
        def welcome(self):
            print("Welcome", self.firstname, self.graduationyear)

cl = Children("Ezan","2","2020")
cl.welcome()

