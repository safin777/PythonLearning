import json # import json module


# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)

# print(y["age"])


#Convert from Python to JSON

#If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
#Example
#Convert from Python to JSON:

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


#https://www.w3schools.com/python/python_json.asp