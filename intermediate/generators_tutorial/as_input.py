# can be an input for functions that use iterables

def my_generator():
    yield 1
    yield 3
    yield 2


g = my_generator()
print(sum(g))

g = my_generator()
a = sorted(g)
print(a)

g = my_generator()
value = next(g)
print(value)
print(sorted(g))

