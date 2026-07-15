import math

# function
""" function : def function_name(parameters):

    function body
    return value
"""


def welcome(name):
    return f"Welcome {name}!"


name = input("Enter your name: ")
print(welcome(name))


# power
def pow(num, power):
    return num**power


print(pow(2, 3))  # 8


# args
def total(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(total(1, 2, 3, 4, 5))  # 15


# kwargs : it is used to pass a variable number of keyword
# arguments to a function. It allows you to handle named arguments
# that you may not have defined in advance.
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


display_info(name="Alice", age=30, city="New York")


# scope : The scope of a variable refers to the region of the code
# where that variable is accessible. In Python, there are four types
# of variable scope: local, enclosing, global, and built-in.
# The types of variable scope in Python are:
# 1. Local Scope: Variables defined within a function are in the
# local scope and can only be accessed within that function.
# 2. Enclosing Scope: This refers to the scope of variables in
# enclosing functions. If a function is nested inside another
# function, the inner function can access variables from the outer
# function.
# 3. Global Scope: Variables defined at the top level of a script or
# module are in the global scope and can be accessed from anywhere in
# the module.
# 4. Built-in Scope: This refers to the scope of built-in functions
# and variables in Python, such as `print()`, `len()`, etc. These are
# always accessible.


# lambda : A lambda function is a small anonymous function that can
# take any number of arguments, but can only have one expression.
# It is defined using the `lambda` keyword. Lambda functions are
# often used for short, simple operations where defining a full
# function would be unnecessary.
def square(x):
    return x**2


print(square(5))  # Output: 25


def length(s):
    return len(s)


print(length("Hello, World!"))  # Output: 13


# sort , lambda
def sort_students(students):
    return sorted(
        students, key=lambda student: student[1]
    )  # Sort by age and sorted doesn't change the original list


students = [("John", 25), ("Alice", 22), ("Bob", 30)]
sorted_students = sort_students(students)
print(sorted_students)  # Output: [('Alice', 22), ('John', 25), ('Bob', 30)]

# args tuple and positional arguments, kwargs dictionary and
# keyword arguments (named arguments)


# areas of circle,triange, rectangle
def area_circle(radius):
    return math.pi * radius**2


print(area_circle(5))  # 78.53981633974483


def area_triangle(base, height):
    return 0.5 * base * height


print(area_triangle(5, 10))  # 25.0


def area_rectangle(length, width):
    return length * width


print(area_rectangle(5, 10))  # 50


# lambdabased sorter
def sorting(students):
    return students.sort(
        key=lambda student: student[1]
    )  # Sort by age; sorted() doesn't change the original list


print(sorting(students))  # Output: [('Alice', 22), ('John', 25), ('Bob', 30)]


# flexible logger system
def flexible_logger(level, message):
    levels = {
        "info": lambda msg: print(f"[INFO]: {msg}"),
        "warning": lambda msg: print(f"[WARNING]: {msg}"),
        "error": lambda msg: print(f"[ERROR]: {msg}"),
    }
    log_function = levels.get(level.lower())
    if log_function:
        log_function(message)
    else:
        print(f"[UNKNOWN LEVEL]: {message}")


# loggerusing args,kwargs
def logger(*message, **details):
    print("Messages")
    for msg in message:
        print(f"- {msg}")
    print()  # it is done to add a new line between messages and details
    print("Details")
    for key, value in details.items():
        print(f"{key}: {value}")


logger("System started", "User logged in", user="Alice", status="active")
