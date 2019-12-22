class Animal:
    def __init__(self, name, color):
        self.name = name  # 'Animal'
        self.color = color  # 'Grey'

    def show(self):
        print(f'My name is {self.name} and I am {self.color}')


# create objects
cat = Animal('Meo', 'silver')
cat.show()

dog = Animal('Hund', 'brown')
dog.show()
