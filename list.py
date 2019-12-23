# Array is called list
fib1 = [1, 1, 2, 3, 5, 8, 13]
print(fib1)

# Traversing array
for num in fib1:
    print(num)

# Length of list
print(f'Length: ', len(fib1))

# String to array
sFruits = 'apple carrot banana orange grapes banana'
fruits = sFruits.split(' ')
print(f'Fruits array:', fruits)
print(f'Number of banana:', fruits.count('banana'))

# Slice lists
slice1 = fruits[0:3]
print(f'Slice 1', slice1)
# Reverse slice - start from -4 counting in reverse, and end at index 4 - non inclusive
slice2 = fruits[-4:4]
print(f'Slice 2 reverse:', slice2)

# Slice from reverse 4 until the end
slice3 = fruits[-4:]
print(f'Slice 3 reverse:', slice3)

# Concatenate
slice4 = slice2 + slice3
print(f'Slice 4 conc:', slice4)
# like wise list.append, list.pop, list.remove

# Array of arrays = list of lists
list2d = [slice1, slice2, slice3]
print(f'2D array', list2d)

# list with diff data types
listData = ['apple', 3, 'banana', 5]
print(listData, type(listData[1]))

# List comprehension - short cut way - double numbers
fib2 = [num * 2 for num in fib1]
print(f'Doubled fib1', fib2)

# List comprehension - even numbers
even = [num for num in fib1 if num % 2 == 0]
print(f'Even fibonocci', even)
