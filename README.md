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
```python
    class Animal:
        def __init__(self, name, color):
            self.name = name
            self.color = color

        def show(self):
            print(f'My name is {self.name} and I am {self.color}')


    cat = Animal('meao', 'gray')

```
   
