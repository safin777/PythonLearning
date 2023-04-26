#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#Lists are created using square brackets:

#Example
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#output: ['apple', 'banana', 'cherry', 'apple', 'cherry']
#allow duplicate values
#Lists are ordered, meaning: the items have a defined order, and that order will not change.


#The list() Constructor
#It is also possible to use the list() constructor when creating a new list.
#Example

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print("This is list() constructor:",thislist)


# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

#Access Items
print(thislist[-2]) #output: banana
thislist.insert(2, "watermelon") # insert method for watermelon
print("inserted list",thislist) #output: ['apple', 'banana', 'watermelon', 'cherry', 'apple', 'cherry']
#append() method
thislist.append("orange")
print("append list",thislist) #output: ['apple', 'banana', 'watermelon', 'cherry', 'apple', 'cherry', 'orange']

# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Remove Item
thislist.remove("banana")
print("remove list",thislist) #output: ['apple', 'watermelon', 'cherry', 'apple', 'cherry', 'orange']
#pop() method
thislist.pop()
print("pop list",thislist) #output: ['apple', 'watermelon', 'cherry', 'apple', 'cherry']


del thislist[0]
print("del:============",thislist)

#The clear() method empties the list:
#thislist.clear()

#Loop Through a List
for x in thislist:
  print("loop through list",x)

for i in range(len(thislist)):
  print(thislist[i])


#List Comprehension
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#Example
#newlist = [expression for item in iterable if condition == True]
newlist = [ x for x in thislist if "a" in x ]
print("List Comprehension",newlist) 
#output : List Comprehension ['mango', 'pineapple']

#Sort Lists
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist.sort()
thislist.sort(reverse=True) # descending order
#custom sort function
#You can also customize your own function by using the keyword argument key = function.
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Copy a List
#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
#There are ways to make a copy, one way is to use the built-in List method copy().
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


#Join Two Lists
#There are several ways to join, or concatenate, two or more lists in Python.
#One of the easiest ways are by using the + operator.
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print("Join Two Lists",list3) #output: ['a', 'b', 'c', 1, 2, 3]

#Another way to join two lists are by appending all the items from list2 into list1, one by one:
for x in list2:
    list1.append(x)
print("Join Two Lists",list1) #output: ['a', 'b', 'c', 1, 2, 3]

#Or you can use the extend() method, which purpose is to add elements from one list to another list:
list1.extend(list2)
print("Join Two Lists",list1) #output: ['a', 'b', 'c', 1, 2, 3]


#list methods
#Method	Description
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list
