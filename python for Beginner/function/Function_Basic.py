## Functions

# 1) How to define a function ?
# 2) How to add the doc string in a function ?
# 3) How to give an argument in the function ?
# 4) Use of the keyword "return"

# 5) Function for addition of two numbers
# 6) Function to return even numbers from a given list

# 1) How to define a function ?

def hello():
    print("Hello")
    
hello
hello()

help(hello)

def my_function():
    """ 
    Created by: Vijay
    Input: No
    Output: Hello
    
    """
    print("Hello")
    
my_function()
help(my_function)


def greeting():
    print("Good Morning")
    
greeting()

# 2) How to give an argument in the function ?

def greeting_arg(name):
    print("Good Morning " + name)
    
greeting_arg("Vijay")


def greeting_(name= "Chris"):
    print("Good Morning " + name)
    
greeting_()
greeting_("Tom")

my_variable = greeting_("Tom")
my_variable
type(my_variable)


# 3) Store data into a variable with "return"

def greeting_return(name = "Mark"):
    return "Hello " + name

greeting_return("Tom")
a = greeting_return("Tom")
a
type(a)

# 4) Define a function for addition of two numbers


def add(n1,n2):
    return n1 + n2

add(70, 30)

b = add(70, 30)
b
# Q: Print the even numbers from the given list


def even_number(l):
    """
    It's a function to print even number's
    input: A list with numbers
    output: A list with even numbers
    """
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return(enum)
    
even_number([1,2,3,4,5,6,7,8,9])
help(even_number)
