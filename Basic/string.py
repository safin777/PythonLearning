a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)  

#output:
# Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.


#####  Slicing Strings #####

_slice_string = "Hello, World!"
print(_slice_string[2:5]) 

#output: llo

######Slice To the End ######
print ("Slice from index[2] to end:",_slice_string[2:])
#output: llo, World!

###### Negative Indexing ######
print ("Negative Indexing:",_slice_string[-5:-2])
#output: orl

###### String Length ######
# It will count the length of the string with white space
print ("String Length:",len(_slice_string))
#output: 13

###### String Methods ######
#https://www.w3schools.com/python/python_strings_methods.asp

# upper()
#lower()
# strip() The strip() method removes any whitespace from the beginning or the end:
# replace() The replace() method replaces a string with another string:
# split() The split() method splits the string into substrings if it finds instances of the separator:
# format() The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
# capitalize() The capitalize() method returns a string where the first character is upper case.
# casefold() The casefold() method returns a string where all the characters are lower case.
# center() The center() method will center align the string, using a specified character (space is default) as the fill character.
# count() The count() method returns the number of times a specified value appears in the string.
# encode() The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
# endswith() The endswith() method returns True if the string ends with the specified value, otherwise False.
# expandtabs() The expandtabs() method sets the tab size to the specified number of whitespaces.
# find() The find() method finds the first occurrence of the specified value.
# format_map() The format_map() method takes a single argument, a dictionary, and replaces placeholders with values from the dictionary.
# index() The index() method finds the first occurrence of the specified value.
# isalnum() The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
# isalpha() The isalpha() method returns True if all the characters are alphabet letters (a-z).
# isdecimal() The isdecimal() method returns True if all the characters are decimals (0-9).
# isdigit() The isdigit() method returns True if all the characters are digits, otherwise False.
# isidentifier() The isidentifier() method returns True if the string is a valid identifier, otherwise False.
# islower() The islower() method returns True if all the characters are in lower case, otherwise False.
# isnumeric() The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
# isprintable() The isprintable() method returns True if all the characters are printable, otherwise False.
# isspace() The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
# istitle() The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
# isupper() The isupper() method returns True if all the characters are in upper case, otherwise False.
# join() The join() method takes all items in an iterable and joins them into one string.
# ljust() The ljust() method will left align the string, using a specified character (space is default) as the fill character.
# lower() The lower() method returns a string where all characters are lower case.
# lstrip() The lstrip() method removes any leading characters (space is the default leading character to remove)
# maketrans() The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.
# partition() The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
# replace() The replace() method replaces a specified phrase with another specified phrase.
# rfind() The rfind() method finds the last occurrence of the specified value.

#format() method Example

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#output: My name is John, and I am 36

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#output: I want 3 pieces of item 567 for 49.95 dollars.


#Python - Escape Characters

# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value


#Example

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#output: We are the so-called "Vikings" from the north.
