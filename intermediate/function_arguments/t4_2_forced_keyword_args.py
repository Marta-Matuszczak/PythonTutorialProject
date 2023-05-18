def foo1(a, b, *, c, d):  # c and d are forced keyword arguments (all after *)
    print(a, b, c, d)


def foo2(*args, b, c):  # b and c are forced keyword arguments (all after *args)
    for a in args:
        print(a)
    print(b, c)


foo1(1, 2, c=3, d=4)
foo2(b=1, c=2)
foo2(1, 2, 3, b=4, c=5)
