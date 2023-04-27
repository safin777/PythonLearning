def personalInfo(name,age,gender):
    personName(name);
    personAge(age);
    personGender(gender);

def personName(name):
    print("My name is===>",name);
def personAge(age):
    print("I am", age ,"years old");
def personGender(gender):
    print("my gender is===>",gender);

personalInfo("safin","26","male");
personalInfo("Sifa","27","female");


#Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def my_function(*kids):
  print("The youngest child is " + kids[2]);
my_function("Emil", "Tobias", "Linus");

#Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def my_function(**kid):
    print("His last name is " + kid["lname"]);
my_function(fname = "Tobias", lname = "Refsnes");

#Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:
def my_function(country = "Norway"):
  print("I am from " + country);
my_function("Sweden");
my_function("India");
my_function();

#Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

def my_function(food):
  for x in food:
    print(x);
fruits = ["apple", "banana", "cherry"];
my_function(fruits);


#the pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
    pass;

#Recursion
# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
# To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1);
        print(result);
    else:
        result = 0;
    return result;
print("\n\nRecursion Example Results");
tri_recursion(6);


