class Employee:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def fullName(self):
        return '{} {}'.format(self.firstName, self.lastName)


emp_1 = Employee('Alex', 'Kan')
emp_2 = Employee('John', 'Doe')

print(emp_1.fullName())
print(emp_2.fullName())
