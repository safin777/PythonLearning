class Vehical :
    def info () : 
        print ("This is a vehical class")
        

#calling class methods

v1 = Vehical()
v1.info


#The init Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
# Example

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

per1 = Person("safin", 21)

print(per1.name)
print(per1.age)


# Note: The __init__() function is called automatically every time the class is being used to create a new object.
# The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
# Example
# Use the words mysillyobject and abc instead of self:
class Person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name = name
        mysillyobject.age = age

per1 = Person("safin", 21)

print(per1.name)
print(per1.age)

#the __str__() method
# The __str__() method is used to display a readable string representation of an object.
# If you try to print an object without having a __str__() method, you would get an unreadable representation of the object.
# Example

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return "Hello my name is " + self.name
    
per1 = Person("safin", 21)
print(per1)

#the pass statement
class Person:
    pass

#the del statement
# The del keyword deletes the object:
# Example
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return "Hello my name is " + self.name
    def __del__(self):
        print("Person object deleted")

per1 = Person("safin", 21)
print(per1)
del per1


