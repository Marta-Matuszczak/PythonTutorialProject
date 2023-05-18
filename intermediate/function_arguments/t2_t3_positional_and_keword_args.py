def foo(a, b, c, d=4):  # d has a default value, default parameters must be at the end
    print(a, b, c, d)


foo(1, 2, 3)  # positional arguments
foo(a=1, b=2, c=3)  # keyword arguments
foo(c=3, a=1, b=2)  # order doesn't matter for keyword arguments
foo(1, c=3, b=2)  # can be mixed but positional arguments always are first
foo(1, 2, 3, 10)  # default argument can be changed
foo(1, b=2, a=3)  # will raise an error
