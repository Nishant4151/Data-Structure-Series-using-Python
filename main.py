# ============================================================
#              PYTHON COMPLETE BASICS NOTES
#              ZERO TO INTERMEDIATE LEVEL
# ============================================================

# 1. PRINT FUNCTION
# Definition: print() is used to display output on the screen.

print("Hello, World!")
print("Welcome to Python")


# ============================================================
# 2. COMMENTS
# Definition: Comments explain code and are ignored by Python.
# Single-line comments start with #.
# Triple-quoted strings can be used as documentation (docstrings).

print("Comments are ignored by Python")


# ============================================================
# 3. VARIABLES
# Definition: Variables are names that refer to objects.

name = "Aashu"
age = 20
salary = 25000.50

print(name)
print(age)
print(salary)


# Multiple Assignment
a, b, c = 10, 20, 30
print(a, b, c)

# Assign Same Value
x = y = z = 100
print(x, y, z)

# Check Data Type
print(type(name))
print(type(age))

# Check Object Identity
# Definition: id() returns the identity of an object.
print(id(age))


# ============================================================
# 4. DATA TYPES
# Definition: Data types classify the values stored in Python.

integer = 100
floating = 10.5
complex_number = 2 + 3j
boolean = True
string = "Python"
my_list = [10, 20, 30]
my_tuple = (10, 20, 30)
my_set = {10, 20, 30}
my_dict = {"name": "Aashu", "age": 20}
nothing = None

print(type(integer))
print(type(floating))
print(type(complex_number))
print(type(boolean))
print(type(string))
print(type(my_list))
print(type(my_tuple))
print(type(my_set))
print(type(my_dict))
print(type(nothing))


# ============================================================
# 5. TYPE CONVERSION
# Definition: Type conversion changes a value from one type
# to another.

print(int("100"))
print(float("10.5"))
print(str(100))
print(bool(1))
print(list((10, 20, 30)))
print(tuple([10, 20, 30]))
print(set([10, 20, 20, 30]))
print(dict(name="Aashu", age=20))
print(complex(2, 3))

# Unicode Conversion
print(ord("A"))
print(chr(65))

# Implicit Type Conversion
a = 10
b = 2.5
print(a + b)

# Explicit Type Conversion
x = 10.8
print(int(x))


# ============================================================
# 6. ARITHMETIC OPERATORS
# Definition: Arithmetic operators perform mathematical
# operations.

a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor Division
print(a % b)   # Modulus
print(a ** b)  # Exponentiation


# ============================================================
# 7. COMPARISON OPERATORS
# Definition: Comparison operators compare two values and
# return True or False.

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# ============================================================
# 8. ASSIGNMENT OPERATORS
# Definition: Assignment operators assign or update values.

x = 10

x += 5
print(x)

x -= 3
print(x)

x *= 2
print(x)

x /= 4
print(x)

x //= 2
print(x)

x **= 2
print(x)

x %= 5
print(x)


# ============================================================
# 9. LOGICAL OPERATORS
# Definition: Logical operators combine or reverse conditions.

a = 10
b = 20

print(a < b and b > 10)
print(a > b or b > 10)
print(not a > b)


# ============================================================
# 10. MEMBERSHIP OPERATORS
# Definition: Membership operators check whether a value
# exists in a collection.

numbers = [10, 20, 30, 40]

print(20 in numbers)
print(50 not in numbers)


# ============================================================
# 11. IDENTITY OPERATORS
# Definition: Identity operators check whether two references
# point to the same object.

a = [10, 20]
b = a
c = [10, 20]

print(a is b)
print(a is c)
print(a == c)
print(a is not c)


# ============================================================
# 12. BITWISE OPERATORS
# Definition: Bitwise operators work with integer binary bits.

a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)


# ============================================================
# 13. USER INPUT
# Definition: input() receives user input as a string.
# Uncomment the examples below to enter values manually.

# name = input("Enter your name: ")
# print(name)

# age = int(input("Enter your age: "))
# print(age)

# a, b = map(int, input("Enter two numbers: ").split())
# print(a + b)

# Executable example without manual input:
name = "Aashu"
print("User:", name)


# ============================================================
# 14. IF STATEMENT
# Definition: if executes code when its condition is True.

age = 20

if age >= 18:
    print("Eligible to vote")


# ============================================================
# 15. IF ELSE
# Definition: if-else chooses between two blocks.

number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# ============================================================
# 16. IF ELIF ELSE
# Definition: elif checks additional conditions.

marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")


# ============================================================
# 17. NESTED IF
# Definition: A nested if is an if statement inside another if.

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Underage")


# ============================================================
# 18. TERNARY OPERATOR
# Definition: A conditional expression selects a value based
# on a condition.

age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)


# ============================================================
# 19. FOR LOOP
# Definition: A for loop iterates over an iterable.

for i in range(1, 6):
    print(i)


# ============================================================
# 20. WHILE LOOP
# Definition: A while loop repeats while its condition is True.

i = 1

while i <= 5:
    print(i)
    i += 1


# ============================================================
# 21. RANGE FUNCTION
# Definition: range() generates a sequence of integers.

print(list(range(5)))
print(list(range(1, 10)))
print(list(range(1, 11, 2)))
print(list(range(10, 0, -1)))


# ============================================================
# 22. BREAK STATEMENT
# Definition: break immediately exits the nearest loop.

for i in range(1, 10):
    if i == 5:
        break
    print(i)


# ============================================================
# 23. CONTINUE STATEMENT
# Definition: continue skips the remaining code in the current
# iteration and moves to the next iteration.

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# ============================================================
# 24. PASS STATEMENT
# Definition: pass is a placeholder that performs no action.

for i in range(5):
    pass

print("Pass executed")


# ============================================================
# 25. NESTED LOOPS
# Definition: A nested loop is a loop inside another loop.

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# ============================================================
# 26. LOOP ELSE
# Definition: A loop's else block executes if the loop
# completes without encountering break.

for i in range(3):
    print(i)
else:
    print("Loop completed")


# ============================================================
# 27. STRINGS
# Definition: Strings are immutable sequences of characters.

text = "Python Programming"

print(text)
print(type(text))
print(len(text))


# ============================================================
# 28. STRING INDEXING
# Definition: Indexing accesses individual characters.

text = "Python"

print(text[0])
print(text[1])
print(text[-1])
print(text[-2])


# ============================================================
# 29. STRING SLICING
# Definition: Slicing extracts part of a sequence.

text = "Python Programming"

print(text[0:6])
print(text[7:])
print(text[:6])
print(text[::2])
print(text[::-1])


# ============================================================
# 30. STRING OPERATIONS
# Definition: Strings support concatenation and repetition.

a = "Hello"
b = "Python"

print(a + " " + b)
print(a * 3)


# ============================================================
# 31. STRING METHODS
# Definition: String methods perform operations on text.

text = "  hello python programming  "

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.strip())
print(text.lstrip())
print(text.rstrip())
print(text.replace("python", "java"))
print(text.split())
print(text.find("python"))
print(text.count("o"))
print(text.startswith("  hello"))
print(text.endswith("  "))
print(text.swapcase())
print(text.casefold())
print(text.center(40, "-"))
print(text.ljust(40, "-"))
print(text.rjust(40, "-"))

print("Python".isalpha())
print("12345".isdigit())
print("Python123".isalnum())
print("   ".isspace())

print("-".join(["Python", "Java", "SQL"]))
print("Python".zfill(10))
print("Python Programming".partition(" "))
print("HelloPython".removeprefix("Hello"))
print("file.csv".removesuffix(".csv"))


# ============================================================
# 32. STRING FORMATTING
# Definition: String formatting inserts values into text.

name = "Aashu"
age = 20

print(f"My name is {name} and my age is {age}")
print("My name is {} and my age is {}".format(name, age))
print("My name is %s and my age is %d" % (name, age))


# ============================================================
# 33. ESCAPE CHARACTERS
# Definition: Escape characters represent special characters.

print("Hello\nPython")
print("Hello\tPython")
print("He said \"Hello\"")
print("C:\\Users\\Python")


# ============================================================
# 34. LIST
# Definition: A list is an ordered, mutable collection that
# allows duplicate values.

numbers = [10, 20, 30, 40, 50]

print(numbers)
print(numbers[0])
print(numbers[-1])
print(numbers[1:4])


# ============================================================
# 35. LIST METHODS
# Definition: List methods modify or inspect lists.

numbers = [10, 20, 30]

numbers.append(40)
print(numbers)

numbers.insert(1, 15)
print(numbers)

numbers.extend([50, 60])
print(numbers)

numbers.remove(20)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(30))
print(numbers.count(10))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

copied = numbers.copy()
print(copied)

numbers.clear()
print(numbers)


# ============================================================
# 36. NESTED LIST
# Definition: A nested list contains other lists.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])
print(matrix[1][2])


# ============================================================
# 37. LIST COMPREHENSION
# Definition: List comprehension creates lists concisely.

squares = [x ** 2 for x in range(1, 6)]
print(squares)

evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)


# ============================================================
# 38. TUPLE
# Definition: A tuple is an ordered, immutable collection.

numbers = (10, 20, 30, 40)

print(numbers)
print(numbers[0])
print(numbers[-1])
print(numbers[1:3])


# ============================================================
# 39. TUPLE METHODS
# Definition: Tuples provide count() and index() methods.

numbers = (10, 20, 20, 30)

print(numbers.count(20))
print(numbers.index(30))


# ============================================================
# 40. TUPLE PACKING AND UNPACKING
# Definition: Packing groups values into a tuple.
# Unpacking assigns tuple elements to variables.

student = ("Aashu", 20, "BCA")

name, age, course = student

print(name)
print(age)
print(course)


# ============================================================
# 41. SET
# Definition: A set is an unordered collection of unique,
# hashable elements.

numbers = {10, 20, 30, 10}

print(numbers)


# ============================================================
# 42. SET METHODS
# Definition: Set methods add, remove, or combine elements.

numbers = {10, 20, 30}

numbers.add(40)
print(numbers)

numbers.update([50, 60])
print(numbers)

numbers.remove(20)
print(numbers)

numbers.discard(100)
print(numbers)


# ============================================================
# 43. SET OPERATIONS
# Definition: Set operations perform mathematical set logic.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a.issubset(b))
print(a.issuperset(b))
print(a.isdisjoint(b))


# ============================================================
# 44. FROZENSET
# Definition: A frozenset is an immutable set.

numbers = frozenset([10, 20, 30])

print(numbers)
print(type(numbers))


# ============================================================
# 45. DICTIONARY
# Definition: A dictionary stores key-value pairs.
# Dictionary keys must be hashable.

student = {
    "name": "Aashu",
    "age": 20,
    "course": "BCA"
}

print(student)
print(student["name"])
print(student.get("age"))


# ============================================================
# 46. DICTIONARY METHODS
# Definition: Dictionary methods access and modify entries.

student = {
    "name": "Aashu",
    "age": 20
}

print(student.keys())
print(student.values())
print(student.items())

student.update({"city": "Noida"})
print(student)

student.setdefault("course", "BCA")
print(student)

student.pop("age")
print(student)

copied = student.copy()
print(copied)


# ============================================================
# 47. DICTIONARY ITERATION
# Definition: Iteration accesses dictionary keys and values.

student = {
    "name": "Aashu",
    "age": 20,
    "course": "BCA"
}

for key, value in student.items():
    print(key, value)


# ============================================================
# 48. DICTIONARY COMPREHENSION
# Definition: Dictionary comprehension creates dictionaries.

squares = {x: x ** 2 for x in range(1, 6)}

print(squares)


# ============================================================
# 49. FUNCTIONS
# Definition: Functions are reusable blocks of code.

def greet():
    print("Hello Python")

greet()


# ============================================================
# 50. FUNCTION PARAMETERS
# Definition: Parameters are variables declared in a function.
# Arguments are values passed when calling a function.

def add(a, b):
    print(a + b)

add(10, 20)


# ============================================================
# 51. RETURN STATEMENT
# Definition: return sends a result back to the caller.

def multiply(a, b):
    return a * b

result = multiply(10, 5)
print(result)


# ============================================================
# 52. DEFAULT ARGUMENTS
# Definition: Default arguments provide fallback values.

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Aashu")


# ============================================================
# 53. KEYWORD ARGUMENTS
# Definition: Keyword arguments specify parameter names.

def student(name, age):
    print(name, age)

student(age=20, name="Aashu")


# ============================================================
# 54. *ARGS
# Definition: *args collects extra positional arguments
# into a tuple.

def total(*args):
    return sum(args)

print(total(10, 20, 30, 40))


# ============================================================
# 55. **KWARGS
# Definition: **kwargs collects extra keyword arguments
# into a dictionary.

def details(**kwargs):
    print(kwargs)

details(name="Aashu", age=20, course="BCA")


# ============================================================
# 56. LAMBDA FUNCTION
# Definition: A lambda is a small anonymous function.

square = lambda x: x ** 2

print(square(5))

addition = lambda a, b: a + b

print(addition(10, 20))


# ============================================================
# 57. RECURSION
# Definition: Recursion occurs when a function calls itself.

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# ============================================================
# 58. LOCAL AND GLOBAL VARIABLES
# Definition: Local variables belong to a function's scope.
# Global variables are defined at module level.

x = 100

def display():
    y = 50
    print("Local:", y)
    print("Global:", x)

display()


# ============================================================
# 59. GLOBAL KEYWORD
# Definition: global allows assignment to a module-level name
# from inside a function.

counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)


# ============================================================
# 60. NONLOCAL KEYWORD
# Definition: nonlocal allows assignment to a variable in
# an enclosing non-global function scope.

def outer():
    x = 10

    def inner():
        nonlocal x
        x += 5

    inner()
    return x

print(outer())


# ============================================================
# 61. BUILT-IN FUNCTIONS
# Definition: Built-in functions are available without imports.

numbers = [10, 20, 30, 40]

print(len(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(abs(-50))
print(round(10.567, 2))
print(pow(2, 3))
print(sorted(numbers, reverse=True))
print(any([False, True, False]))
print(all([True, True, True]))
print(isinstance(10, int))
print(callable(print))


# ============================================================
# 62. ENUMERATE
# Definition: enumerate() produces index-value pairs.

fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


# ============================================================
# 63. ZIP
# Definition: zip() combines elements from iterables.

names = ["Aashu", "Rahul", "Amit"]
ages = [20, 21, 22]

for name, age in zip(names, ages):
    print(name, age)


# ============================================================
# 64. MAP
# Definition: map() applies a function to iterable elements.

numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x ** 2, numbers))

print(squares)


# ============================================================
# 65. FILTER
# Definition: filter() keeps elements satisfying a condition.

numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)


# ============================================================
# 66. SORTED
# Definition: sorted() returns a new sorted list.

numbers = [50, 10, 40, 20, 30]

print(sorted(numbers))
print(sorted(numbers, reverse=True))


# ============================================================
# 67. REVERSED
# Definition: reversed() returns a reverse iterator.

numbers = [10, 20, 30, 40]

print(list(reversed(numbers)))


# ============================================================
# 68. ITERATOR
# Definition: An iterator produces elements one at a time.
# iter() creates an iterator; next() retrieves its next item.

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# ============================================================
# 69. GENERATOR
# Definition: A generator produces values lazily using yield.

def generate_numbers():
    for i in range(1, 6):
        yield i

for number in generate_numbers():
    print(number)


# ============================================================
# 70. DECORATOR
# Definition: A decorator wraps or modifies a callable.

def decorator(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


@decorator
def hello():
    print("Hello World")

hello()


# ============================================================
# 71. EXCEPTION HANDLING
# Definition: Exception handling manages runtime errors.

try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")


# ============================================================
# 72. MULTIPLE EXCEPT BLOCKS
# Definition: Different exceptions can be handled separately.

try:
    number = int("abc")

except ValueError:
    print("Invalid number")

except TypeError:
    print("Invalid type")


# ============================================================
# 73. TRY EXCEPT ELSE FINALLY
# Definition: else runs when no exception occurs.
# finally normally runs regardless of the result.

try:
    result = 10 / 2

except ZeroDivisionError:
    print("Division error")

else:
    print("Result:", result)

finally:
    print("Execution completed")


# ============================================================
# 74. RAISE
# Definition: raise explicitly triggers an exception.

try:
    age = -5

    if age < 0:
        raise ValueError("Age cannot be negative")

except ValueError as error:
    print(error)


# ============================================================
# 75. ASSERT
# Definition: assert checks an assumption during debugging.
# Assertions can be disabled with Python optimization flags.

x = 10

assert x > 0, "Value must be positive"

print("Assertion passed")


# ============================================================
# 76. FILE HANDLING
# Definition: File handling reads and writes persistent data.
# with automatically manages closing the file.

with open("demo.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python\n")
    file.write("Welcome to File Handling\n")

with open("demo.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)


# ============================================================
# 77. FILE APPENDING
# Definition: Append mode adds data to the end of a file.

with open("demo.txt", "a", encoding="utf-8") as file:
    file.write("New Line Added\n")


# ============================================================
# 78. READLINES
# Definition: readlines() returns a list of file lines.

with open("demo.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)


# ============================================================
# 79. FILE POINTER
# Definition: tell() reports the current file position.
# seek() changes the file position.

with open("demo.txt", "r", encoding="utf-8") as file:
    print(file.tell())
    print(file.read(5))
    print(file.tell())
    file.seek(0)
    print(file.read(5))


# ============================================================
# 80. OOP - CLASS AND OBJECT
# Definition: A class defines the structure and behavior
# of objects. An object is an instance of a class.

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


s1 = Student("Aashu", 20)
s1.display()


# ============================================================
# 81. CONSTRUCTOR
# Definition: __init__ initializes a newly created instance.

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


e1 = Employee("Rahul", 30000)

print(e1.name)
print(e1.salary)


# ============================================================
# 82. INHERITANCE
# Definition: Inheritance allows a class to reuse or extend
# behavior from another class.

class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def bark(self):
        print("Dog Barking")


d = Dog()

d.sound()
d.bark()


# ============================================================
# 83. MULTILEVEL INHERITANCE
# Definition: A class inherits from a class that itself
# inherits from another class.

class A:
    def show_a(self):
        print("Class A")

class B(A):
    def show_b(self):
        print("Class B")

class C(B):
    def show_c(self):
        print("Class C")


obj = C()

obj.show_a()
obj.show_b()
obj.show_c()


# ============================================================
# 84. MULTIPLE INHERITANCE
# Definition: A class inherits from more than one parent class.

class Father:
    def father_method(self):
        print("Father Method")

class Mother:
    def mother_method(self):
        print("Mother Method")

class Child(Father, Mother):
    pass


child = Child()

child.father_method()
child.mother_method()


# ============================================================
# 85. POLYMORPHISM
# Definition: Different objects can provide the same interface
# with different behavior.

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")


for animal in [Dog(), Cat()]:
    animal.sound()


# ============================================================
# 86. ENCAPSULATION
# Definition: Encapsulation groups data and related behavior.
# Double underscores trigger name mangling, not true privacy.

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

print(account.get_balance())


# ============================================================
# 87. ABSTRACTION
# Definition: Abstraction exposes essential behavior while
# hiding implementation details.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(10, 5)

print(rectangle.area())


# ============================================================
# 88. CLASS METHOD
# Definition: A class method receives the class as its
# first argument, conventionally named cls.

class Student:

    college = "ABC College"

    @classmethod
    def display_college(cls):
        print(cls.college)


Student.display_college()


# ============================================================
# 89. STATIC METHOD
# Definition: A static method does not automatically receive
# an instance or class argument.

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))


# ============================================================
# 90. METHOD OVERRIDING
# Definition: A child class provides its own implementation
# of a method inherited from a parent.

class Parent:
    def display(self):
        print("Parent Method")

class Child(Parent):
    def display(self):
        print("Child Method")


obj = Child()
obj.display()


# ============================================================
# 91. SUPER FUNCTION
# Definition: super() provides access to methods of the
# next class in the method resolution order.

class Parent:
    def display(self):
        print("Parent Display")

class Child(Parent):
    def display(self):
        super().display()
        print("Child Display")


Child().display()


# ============================================================
# 92. MAGIC METHODS
# Definition: Special methods define behavior for built-in
# operations such as printing, addition, and comparison.

class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"


person = Person("Aashu")

print(person)


# ============================================================
# 93. MODULES
# Definition: Modules are Python files containing reusable code.

import math

print(math.sqrt(25))
print(math.factorial(5))
print(math.pi)
print(math.ceil(10.2))
print(math.floor(10.8))


# ============================================================
# 94. RANDOM MODULE
# Definition: random provides pseudorandom number generation.
# It should not be used for security-sensitive random values.

import random

print(random.randint(1, 10))
print(random.choice(["Apple", "Mango", "Banana"]))
print(random.random())


# ============================================================
# 95. DATETIME MODULE
# Definition: datetime provides date and time functionality.

from datetime import datetime, date, timedelta

print(date.today())
print(datetime.now())

today = datetime.now()

print(today.strftime("%d-%m-%Y"))
print(today.strftime("%A"))
print(today.strftime("%B"))

tomorrow = date.today() + timedelta(days=1)

print(tomorrow)


# ============================================================
# 96. REGULAR EXPRESSIONS
# Definition: Regex matches text using patterns.

import re

text = "My number is 9876543210"

print(re.findall(r"\d+", text))
print(re.search(r"\d+", text).group())
print(re.sub(r"\d", "*", text))
print(re.split(r"\s+", text))


# ============================================================
# 97. JSON
# Definition: JSON is a text format for structured data.

import json

student = {
    "name": "Aashu",
    "age": 20,
    "course": "BCA"
}

json_data = json.dumps(student, indent=4)

print(json_data)

python_data = json.loads(json_data)

print(python_data)
print(python_data["name"])


# ============================================================
# 98. CSV FILES
# Definition: CSV stores tabular data as delimited text.

import csv

with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["Aashu", 20, "BCA"])
    writer.writerow(["Rahul", 21, "BCA"])


with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# ============================================================
# 99. SHALLOW COPY
# Definition: A shallow copy creates a new outer object
# while nested objects may remain shared.

import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)

shallow[0][0] = 100

print(original)
print(shallow)


# ============================================================
# 100. DEEP COPY
# Definition: A deep copy recursively copies nested objects.

original = [[1, 2], [3, 4]]

deep = copy.deepcopy(original)

deep[0][0] = 100

print(original)
print(deep)


# ============================================================
# 101. MUTABLE VS IMMUTABLE
# Definition: Mutable objects can change after creation.
# Immutable objects cannot be modified in place.

numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)

text = "Python"

new_text = text.replace("P", "J")

print(text)
print(new_text)


# ============================================================
# 102. SET COMPREHENSION
# Definition: Set comprehension constructs a set.

squares = {x ** 2 for x in range(1, 6)}

print(squares)


# ============================================================
# 103. GENERATOR EXPRESSION
# Definition: A generator expression produces values lazily.

numbers = (x ** 2 for x in range(1, 6))

print(list(numbers))


# ============================================================
# 104. MATCH CASE
# Definition: match-case performs structural pattern matching.
# Requires Python 3.10 or newer.

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Other Day")


# ============================================================
# 105. TYPE HINTS
# Definition: Type hints document expected types.
# Python does not enforce them automatically at runtime.

def addition(a: int, b: int) -> int:
    return a + b

print(addition(10, 20))


# ============================================================
# 106. DATACLASS
# Definition: A dataclass automatically generates common
# methods for classes primarily used to store data.

from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    age: int
    salary: float


employee = Employee("Aashu", 20, 30000.0)

print(employee)


# ============================================================
# 107. COLLECTIONS - COUNTER
# Definition: Counter counts hashable elements.

from collections import Counter

numbers = [1, 2, 2, 3, 3, 3, 4]

frequency = Counter(numbers)

print(frequency)


# ============================================================
# 108. COLLECTIONS - DEFAULTDICT
# Definition: defaultdict supplies default values for
# missing keys using a factory function.

from collections import defaultdict

marks = defaultdict(int)

marks["Python"] += 10

print(marks["Python"])
print(marks["SQL"])


# ============================================================
# 109. ITERTOOLS
# Definition: itertools provides tools for working with
# iterators efficiently.

from itertools import combinations, permutations

numbers = [1, 2, 3]

print(list(combinations(numbers, 2)))
print(list(permutations(numbers, 2)))


# ============================================================
# 110. FUNCTOOLS - REDUCE
# Definition: reduce() repeatedly combines iterable elements.

from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a + b, numbers)

print(result)


# ============================================================
# 111. PATHLIB
# Definition: pathlib provides object-oriented filesystem paths.

from pathlib import Path

file_path = Path("demo.txt")

print(file_path.exists())
print(file_path.name)
print(file_path.suffix)
print(file_path.resolve())


# ============================================================
# 112. OS MODULE
# Definition: os provides operating-system-related functions.

import os

print(os.getcwd())
print(os.name)
print(os.path.exists("demo.txt"))


# ============================================================
# 113. SYS MODULE
# Definition: sys provides access to interpreter information.

import sys

print(sys.version)
print(sys.platform)
print(sys.executable)


# ============================================================
# 114. LOGGING
# Definition: Logging records events and diagnostic messages.

import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program started")
logging.warning("This is a warning")


# ============================================================
# 115. CUSTOM EXCEPTION
# Definition: Custom exceptions represent application-specific
# error conditions.

class InvalidAgeError(Exception):
    pass


try:
    age = -10

    if age < 0:
        raise InvalidAgeError("Invalid Age")

except InvalidAgeError as error:
    print(error)


# ============================================================
# 116. CLOSURE
# Definition: A closure retains access to variables from
# its enclosing function after that function returns.

def outer_function(message):

    def inner_function():
        print(message)

    return inner_function


my_function = outer_function("Hello from Closure")

my_function()


# ============================================================
# 117. CONTEXT MANAGER
# Definition: A context manager controls setup and cleanup
# when entering and leaving a with block.

from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering context")
    try:
        yield
    finally:
        print("Leaving context")


with my_context():
    print("Inside context")


# ============================================================
# 118. WALRUS OPERATOR
# Definition: := assigns a value within an expression.
# Requires Python 3.8 or newer.

numbers = [10, 20, 30, 40]

if (length := len(numbers)) > 3:
    print("List length:", length)


# ============================================================
# 119. ANY AND ALL
# Definition: any() checks if at least one item is truthy.
# all() checks if every item is truthy.

values = [True, False, True]

print(any(values))
print(all(values))


# ============================================================
# 120. FINAL PRACTICE PROGRAM
# Definition: This program combines variables, lists,
# dictionaries, functions, loops, and conditions.

employees = [
    {"name": "Aashu", "salary": 30000},
    {"name": "Rahul", "salary": 25000},
    {"name": "Amit", "salary": 40000},
    {"name": "Neha", "salary": 35000}
]


def calculate_average_salary(data):
    total_salary = sum(emp["salary"] for emp in data)
    return total_salary / len(data) if data else 0


def highest_paid_employee(data):
    return max(data, key=lambda emp: emp["salary"]) if data else None


def filter_employees(data, minimum_salary):
    return [
        emp for emp in data
        if emp["salary"] >= minimum_salary
    ]


print("\nEMPLOYEE DATA ANALYSIS")

print("Total Employees:", len(employees))

print(
    "Average Salary:",
    calculate_average_salary(employees)
)

print(
    "Highest Paid Employee:",
    highest_paid_employee(employees)
)

print(
    "Employees earning 30000 or more:",
    filter_employees(employees, 30000)
)


# ============================================================
#                   END OF PYTHON NOTES
# ============================================================

print("\nAll Python examples executed successfully!")