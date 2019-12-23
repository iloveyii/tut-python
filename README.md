Python Tutorial
=====================================

In this repo we are practicing Python. We will cover all the important topics.

## Installations
  * Clone the repo `https://github.com/iloveyii/python_tut/`.
  * Run the script as 
```bash
   python3.6 example.py
``` 
## Variables
### Numbers
### Strings

## Control Structures
It controls the flow of execution of statements. These are if elif, for, while.
### if
```python
# IF statement
experience = 7
if experience > 5:
    print('You are a professor')
elif experience > 3:
    print('You are an assistant professor')
else:
    print('You are a lecturer')
```

### for loop
```
fruits = ['banana', 'orange', 'banana', 'orange', 'grapes', 'banana']
print('For loop:')
for fruit in fruits:
    print(fruit)
```

### while loop
```
count = len(fruits)
print('While loop')
while count > 0:
    print(count, fruits[count-1])
    count -= 1
```

## Data Structures
Data structures are used to store data and are complex than simple variables. There are several operations that could
be performed on data structures. Here we discuss List, Set and Dictionary data structure.
### List 
A list is an array just like in other programming languages. An array can contains numbers or strings or both.
It uses square brackets and is 0 indexed. It can count number of matching items easily.
```python
# Array is called list
fib1 = [1, 1, 2, 3, 5, 8, 13]
print(fib1)

# Traversing array
for num in fib1:
    print(num)
```

### List comprehensions
This is a shortcut way of doing operations on list. For example double the values in list.
```python
# List comprehension - short cut way - double numbers
fib2 = [num * 2 for num in fib1]
print(f'Doubled fib1', fib2)
```


### Set
A set is simply a list without duplicates.
```python
fruits = ['banana', 'orange', 'banana', 'orange', 'grapes', 'banana']
sets = set(fruits)
print(f'Set with no duplicates', sets)
```
 
### Dictionary 
A dictionary is like JS json i.e. a key value structure.


  
  
## Classes
  Classes are defined as usual (other languages) with keyword class. The constructor method is called __init__. 
  There is an extra parameter 'self' in all the methods definitions though. There is no need of new in object instantiation.
  Class level attributes can be declared at the start of class (food) and accessed 
  directly either by class `Animal.eats` or object `cat.eats`.
```python
    class Animal:
        eats = 'food'
        def __init__(self, name, color):
            self.name = name
            self.color = color

        def show(self):
            print(f'My name is {self.name} and I am {self.color}')


    cat = Animal('meao', 'gray')

```

There are no concept of private, protect or public access modifiers in Python. This result 
is achieved by using annotated class and static methods. The former has access to only class
level properties (eats) while the later has no access to neither class level and nor object level
attributes.
```python
    
    # Can access only class level attributes
    @classmethod
    def showEating(cls):
        print(f'I eat {cls.eats}')

    @staticmethod
    def alsoEating(food):
        print(f'I also eat {food}')
```
   
## Modules
Modules are logically separated files that provides some functionality to your program.
A module is a file that can be imported. It can be a variable or a function.
```python
    from m1 import PI
    from m1 import area
    
    print(area(3))
    print(f'Value of PI is', PI)
```

## Packages
Splitting related files (which may contain functions and classes) into separate directories is a package.
Code in packages could be easily maintained and debugged.
To declare a directory as a package just place an empty file with name `__init__.py` as shown below.
```python
    |- package
    |-- __init__.py
    |-- circle.py
```
A package could be used as:
```python
from package.circle import Circle


circle = Circle(3)
print(f'Area of circle is', circle.area())
print(f'Circumference of circle is', circle.circumference())
```
Result:
```python
Area of circle is 28.26
Circumference of circle is 18.84
```


