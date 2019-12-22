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
  Class level attributes (static) can be declared at the start of class (food) and accessed 
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
   
