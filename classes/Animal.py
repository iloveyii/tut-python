class Animal:
    def __init__(self):
        self.name = 'Animal'
        self.color = 'Grey'

    def show(self):
        print(f'My name is {self.name} and I am {self.color}')


# create objects
cat = Animal()
cat.show()

dog = Animal()
dog.show()
