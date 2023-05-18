# a parameter marked with * can pass any number of positional arguments to the function (usually called args)
# a parameter marked with ** can pass any number of keyword arguments to the function (usually called kwargs)
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, " - ", kwargs[key])


foo(1, 2, 3, 4, five=5, six=6, seven=7)
print()
foo(1, 2, five=5, six=6, seven=7)
print()
foo(1, 2, 3, 4)
