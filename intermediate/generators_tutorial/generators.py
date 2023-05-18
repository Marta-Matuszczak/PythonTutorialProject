# function that can return an object that can be iterated over. More memory efficient with large amount of data
# generators use lazy loading, which means they return only one at a time, only when needed

def my_generator():
    yield 1
    yield 2
    yield 3


g = my_generator()

value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)


