class Animal:
    eats = 'food'

    def __init__(self, name, color):
        self.name = name  # 'Animal'
        self.color = color  # 'Grey'

    def show(self):
        print(f'My name is {self.name} and I am {self.color}')

    # Can access only class level attributes
    @classmethod
    def showEating(cls):
        print(f'I eat {cls.eats}')

    @staticmethod
    def alsoEating(food):
        print(f'I also eat {food}')


# create objects
cat = Animal('Meo', 'silver')
cat.show()
print(Animal.eats)

dog = Animal('Hund', 'brown')
dog.show()
print(dog.eats)
dog.showEating()
dog.alsoEating('meat')