"""Comprehensive Practice Question 1

Create a Python program for a College Student Management System.

Your program must satisfy all of the following:

A. Class and Objects

Create a class:

Student

with:

name
roll_no
marks

Use a constructor __init__() to initialize them.

Create two Student objects.

B. Instance Variable

name, roll_no, and marks must be instance variables.

Create a method:

display()

that displays the student's information.

C. Class/Static Variable

Create a class variable:

college = "MIT"

Display the college name using both Student objects.

D. Instance Method

Create:

def calculate_grade(self):

Use the marks to return:

90+  → A
75-89 → B
60-74 → C
40-59 → D
Below 40 → Fail
E. Static Method

Create a static method:

@staticmethod
def is_valid_marks(marks):

Return True if marks are between 0 and 100, otherwise False.

F. Inheritance

Create:

Student
   ↓
EngineeringStudent

EngineeringStudent should have an additional variable:

branch

and method:

display_branch()
G. Polymorphism / Method Overriding

Create a display() method inside EngineeringStudent that behaves differently from the parent's display() method.

For example, it should display:

Name
Roll No
Marks
College
Branch
H. Encapsulation

Make marks private:

__marks

Create:

get_marks()
set_marks()

to access/change marks.

The setter should reject marks outside 0–100.

I. Abstraction

Create an abstract class:

Person

with an abstract method:

display_role()

Then make Student implement it.

J. Magic Method

Implement:

__str__()

so that:

print(student)

prints meaningful student information instead of the default object representation.

Your program should demonstrate:
✓ Class
✓ Objects
✓ __init__()
✓ self
✓ Instance variables
✓ Class variable
✓ Instance method
✓ Static method
✓ Inheritance
✓ Polymorphism
✓ Encapsulation
✓ Abstraction
✓ Magic method

These are the core concepts covered in Topic 1 of your PDF."""
class Student:
    college = "MIT"
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
# Instance Methods: These are regular methods defined inside a class and operate on instances of that class. They automatically take self (the instance) as the first
# argument.    
    def display(self):          #Instance Method
        print(self.name)
        print(self.roll_no)
        print(self.marks)
#Static Methods: These methods are decorated with @staticmethod and are independent of the class and instance state. They don't automatically pass self or cls
#as the first argument.
    @staticmethod
    def is_marks_valid(marks):
        if marks < 0 or marks > 100:
            print("Invalid marks")
        else:
            print("Valid marks")

    def calculate_grade(self):  #Instance Method
        match self.marks:
            case self.marks if self.marks >= 45 and self.marks <=100:  # case variable if variable condition and variable condition: #And not case 1 or case 2
                print("PASS")
            case self.marks if self.marks < 45:
                print("FAIL")
class EngineeringStudents(Student):
    #super() is used in a subclass to access the parent class's methods or constructor.
    def __init__(self,name,roll_no,marks,branch): #While making subcalss constructor we need to add the parent class attributes in the subclass constructor as well + subclass attributes
        super().__init__(name,roll_no,marks)  # Call the parent class's constructor to initialize inherited attributes
        self.branch = branch
    def display_branch(self):
        print(self.branch) 
    def display(self):
        print("Name: " + self.name)
        print("Roll No: " + str(self.roll_no))
        print("Marks: " + str(self.marks))
        print("Branch: " + self.branch)

# s1 = Student("Sumeet",57,72.90)
s2 = Student("Krutik",27,80)
s1 = EngineeringStudents("Sumeet",57,72.90,"Computer Science")

# s1.display()
s1.display() #polymorphism example as we have 2 display method one in student class and one in engineering student class. So when we call display method on s1 object which is of type EngineeringStudent it calls the display method of EngineeringStudent class instead of Student class.
s1.is_marks_valid(s1.marks)
s1.calculate_grade()
print(s1.college)

s2.display()
s2.is_marks_valid(s2.marks)
s2.calculate_grade()
print(s2.college)

#===============================================================================================================================================================================================================================================================================================#
# Encapsulation: Making marks private and providing getter and setter methods to access and modify it.
class Student:
    college = "MIT"
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.__marks = marks  # Private variable

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks. Please enter a value between 0 and 100.")

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.__marks}")

s3 = Student("Alice", 101, 85)
s3.display()  # Display initial marks
s3.set_marks(90)  # Update marks using setter
s3.display()  # Display updated marks
#===============================================================================================================================================================================================================================================================================================#
#Abstraction --> Abstraction = Parent class sets the rule → Child class must follow the rule.
from abc import ABC, abstractmethod

# Abstract class
class Person(ABC):

    @abstractmethod
    def display_role(self):
        pass


# Child class
class Student(Person):

    def display_role(self):
        print("Role: Student")


student = Student()
student.display_role()
#===============================================================================================================================================================================================================================================================================================#
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Name: {self.name}, Marks: {self.marks}"


#without __str__ method, it would print something like <__main__.Student object at 0x...> which is not meaningful.
class Students:   #class without __str__ method
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

student = Students("Sumeet", 85)
print("Without __str__ method:\n", student)  # This will print the default object representation, which is not meaningful.

student = Student("Sumeet", 85)
print("With __str__ method:\n",student)  # This will call the __str__ method and print meaningful information