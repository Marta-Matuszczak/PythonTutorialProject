def foo(a, b, *, c, d):
    print(a, b, c, d)


foo("a", 3, c=5, d="0")
