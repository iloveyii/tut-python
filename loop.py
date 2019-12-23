# For loop
fruits = ['banana', 'orange', 'banana', 'orange', 'grapes', 'banana']
print('For loop:')
for fruit in fruits:
    print(fruit)

# While loop
count = len(fruits)
print('While loop')
while count > 0:
    print(count, fruits[count-1])
    count -= 1

