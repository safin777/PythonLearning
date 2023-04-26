# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

# Example

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# output: ('apple', 'banana', 'cherry')
# Tuples are unchangeable, meaning that you cannot change, add or remove items after the tuple has been created.

#tuple constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print("tuple constructor",thistuple)
