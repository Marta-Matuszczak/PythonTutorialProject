def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")


foo(1, 2, 4, 5, 6, seven=7, eight=8)
