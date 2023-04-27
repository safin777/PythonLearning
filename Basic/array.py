#Array of Pyhton
#Array is a collection of similar data type

#Array declaration
#Array is declared as follows:
# arrayName = [data1,data2,data3,....]
# Example

cars = ["Ford", "Volvo", "BMW"]
print(cars)

#Accessing Array Elements
#Array elements are accessed by their index number:
# Example
x = cars[0]
print(x)

#Modify Array Elements
#You modify an element of an array by referring to the index number:
# Example
cars[0] = "Toyota"
print(cars)


#Array Length
#Use the len() method to return the length of an array (the number of elements in an array).
# Example
x = len(cars)
print(x)

#Looping Array Elements
#You can use the for in loop to loop through all the elements of an array.
# Example
for x in cars:
    print(x)

#Adding Array Elements
#You can use the append() method to add an element to an array.
# Example
cars.append("Honda")
print(cars)

#Removing Array Elements
#You can use the pop() method to remove an element from the array.
# Example
cars.pop(1)
print(cars)

#You can also use the remove() method to remove an element from the array.
# Example
cars.remove("BMW")
print(cars)

#Array Methods
#Python has a set of built-in methods that you can use on lists/arrays.
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.