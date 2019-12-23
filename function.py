# function with a single parameter
def area(r):
    return 3.14 * r ** 2


# function with parameters default value
def area2(r, pi=3.14):
    return pi * r ** 2


print(area(3))
print(area2(3))
