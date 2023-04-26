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