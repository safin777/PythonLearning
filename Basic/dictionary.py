# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# Dictionaries are written with curly brackets, and have keys and values:
# Example
# Create and print a dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])
print(thisdict["model"])    
print(thisdict["year"])

#changeable value
# not allow duplicate values
# not allow duplicate keys
# ordered* (as of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.)

# The dict() Constructor
# It is also possible to use the dict() constructor to make a new dictionary:
# Example
# Create a new dictionary using the dict() constructor:
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
# Example

x = thisdict["model"]
print(x)
g = thisdict.get("model")
print(g)

#get keys
print(thisdict.keys())
#get values
print(thisdict.values())


#Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
# Example

print(thisdict.items())

# Change Values
# You can change the value of a specific item by referring to its key name:
# Example

thisdict["year"] = 2018
print(thisdict)

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
# Example

thisdict.update({"year": 2020})

# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
# Example

thisdict["color"] = "red"
thisdict.update({"weight": "10ton"})
print(thisdict)


# Removing Items
# There are several methods to remove items from a dictionary:
# Example

# The pop() method removes the item with the specified key name:
thisdict.pop("model")
#thisdict.popitem()
#del thisdict["model"]
#print(thisdict)
#thisdict.clear()
#del thisdict



# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
# Example

for x in thisdict:
    print(x," values are =>" , thisdict[x])

#keys
for x in thisdict.keys():
    print(x)


#values
for x in thisdict.values():
    print(x)

#items
for x,y in thisdict.items():
    print(x,"====>",y)



# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
# Example

mydict = thisdict.copy()
print(mydict)

# Another way to make a copy is to use the built-in function dict().
# Example

mydict = dict(thisdict)
print(mydict)

# Nested Dictionaries
# A dictionary can also contain many dictionaries, this is called nested dictionaries.
# Example

myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }

}
print(myfamily)

# Or, if you want to nest three dictionaries that already exists as dictionaries:
# Example

child1 = {
    "name" : "Emil",
    "year" : 2004
}
child2 = {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name" : "Linus",
    "year" : 2011
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

print(myfamily)

# The dict() Constructor
# It is also possible to use the dict() constructor to make a new dictionary:
# Example

thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

# Dictionary Methods
# Python has a set of built-in methods that you can use on dictionaries.
# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary
