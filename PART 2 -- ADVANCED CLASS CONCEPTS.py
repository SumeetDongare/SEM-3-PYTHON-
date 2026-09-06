"""
PART 2 — ADVANCED CLASS CONCEPTS
Comprehensive Practice Question 2

Create a Number Processing System that demonstrates all the advanced Python concepts from Topic 2.

Your program must contain the following.

A. Function Decorator

Create a decorator:

@log_function

It should print:

Function started
Function finished

before and after the decorated function executes.

B. Decorator with Arguments

Create a function:

add(a, b)

and decorate it.

The decorator must support arguments using:

*args
**kwargs
C. Method Decorator

Create a class:

Calculator

with a method:

multiply(a, b)

Apply your decorator to this method.

D. Class Decorator

Create a class decorator that adds a method:

show_message()

to a class.

When called, it should print:

Hello from class decorator
E. @staticmethod

Inside Calculator, create:

@staticmethod
square(n)

which returns:

n × n
F. @classmethod

Create a class:

NumberSystem

with a class variable:

system = "Decimal"

Create:

@classmethod
show_system(cls)

that displays the number system.

G. @property

Create a class:

Circle

with:

radius

Create a property:

@property
def area(self):

which returns:

3.14 × radius × radius

Call it as:

circle.area

not:

circle.area()
H. Iterator

Create your own iterator class:

NumberIterator

that generates numbers from:

1 → n

You must implement:

__iter__()
__next__()

When there are no more numbers, use:

raise StopIteration
I. Generator

Create a generator:

even_numbers(n)

that uses yield to generate all even numbers from 1 to n.

Example:

even_numbers(10)

should produce:

2
4
6
8
10
J. Generator State

Create another generator that produces powers of 2:

1
2
4
8
16
...

using yield.

K. Closure

Create a function:

create_multiplier(x)

that returns an inner function.

For example:

double = create_multiplier(2)

print(double(5))
print(double(10))

Output:

10
20

The inner function must remember x even after the outer function finishes.

Your program should demonstrate:
✓ Function decorator
✓ Decorator with *args/**kwargs
✓ Method decorator
✓ Class decorator
✓ @staticmethod
✓ @classmethod
✓ @property
✓ Iterator
✓ __iter__()
✓ __next__()
✓ StopIteration
✓ Generator
✓ yield
✓ Generator state
✓ Closure
"""
# ============================================================
# PART 2: ADVANCED CLASS CONCEPTS
# ============================================================


# ============================================================
# 1. FUNCTION DECORATOR
#    Supports *args and **kwargs
# ============================================================
def log_function(func):
    def wrapper(*args,**kwargs):  
        #*args collects multiple positional arguments (e.g., func(10, 20) → args = (10, 20)), while **kwargs collects multiple keyword arguments (e.g., func(name="Sumeet") → kwargs = {"name": "Sumeet"})
        #wrapper uses *args and **kwargs so the decorator can work with functions having any number and type of arguments.
        print("Function started")
        result = func(*args,**kwargs)  #wrapper(*args, **kwargs) → receives any arguments.
                                        #func(*args, **kwargs) → passes them to the original function.
        print("Function Finished")
        return result
    return wrapper

@log_function
def add(a,b):
    return a+b

print("Addition: " ,add(10,20))

# ============================================================
# 2. METHOD DECORATOR :- A method decorator is a function that adds extra functionality to a method without changing the method's original code.
# ============================================================
def log_function(func):
    def wrapper(*args,**kwargs):  
        #*args collects multiple positional arguments (e.g., func(10, 20) → args = (10, 20)), while **kwargs collects multiple keyword arguments (e.g., func(name="Sumeet") → kwargs = {"name": "Sumeet"})
        #wrapper uses *args and **kwargs so the decorator can work with functions having any number and type of arguments.
        print("Function started")
        result = func(*args,**kwargs)  #wrapper(*args, **kwargs) → receives any arguments.
                                        #func(*args, **kwargs) → passes them to the original function.
        print("Function Finished")
        return result
    return wrapper

class student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    @log_function
    def display(self):
        print(f"Student Information \n 1.Students Name:{self.name} \n 2.Students Marks: {self.marks}")

s1 = student("Sumeet",72.90)
s1.display()

#Note:-
#*args contains the values for the original function's parameters, e.g., args = (s1, "Hello") → display(self, message) receives self = s1 and message = "Hello".

# ============================================================
# 4. CLASS DECORATOR :- A class decorator is a function that receives a class, modifies or adds features to it, and returns the modified class.
# ============================================================

def add_show_message_method(cls):  #Why cls? ---> The class decorator receives the class itself
    def show_message(self):        #show_message becomes a method of the Message class.
        print("Hello i am a class decorator")

    cls.show_message = show_message #Add show_message to the Message class.
    return cls

@add_show_message_method
class message():
    pass

mssg = message()
mssg.show_message()

# ============================================================
# 5. CLASS METHOD :- It means a class method works with information shared by the whole class, not information belonging to one individual object. i.e class methods can access and modify class variables, which are shared among all instances of the class. They are defined using the @classmethod decorator and take cls as their first parameter, which refers to the class itself.
# ============================================================

class NumberSystem:

    # Class variable
    system = "Decimal"

    @classmethod
    def show_system(cls):
        print("\nNumber System:", cls.system)


NumberSystem.show_system()

# ============================================================
# 6. PROPERTY DECORATOR :- @property makes a method behave like an attribute/variable.
# ============================================================
class circle:
    def __init__(self,radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius * self.radius

Circle = circle(5)
print("Area of circle: ",Circle.area)

# ============================================================
# 7. CUSTOM ITERATOR :- A custom iterator is a user-defined object that uses __iter__() and __next__() to control how values are returned one by one.For loo use it internally
# ============================================================

class numberiterator:
    def __init__(self,n):
        self.n = n
        self.current = 1

    def __iterator__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current +=1

        return value
        

