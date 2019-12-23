Python Tutorial
=====================================

In this repo we are practicing Python. We will cover all the important topics.

## Installations
  * Clone the repo `https://github.com/iloveyii/python_tut/`.
  * Run the script as 
```bash
   python3.6 example.py
``` 
  
  
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
A module is a file that can be imported. It can be a variable or a function.
```python
    from m1 import PI
    from m1 import area
    
    print(area(3))
    print(f'Value of PI is', PI)
```