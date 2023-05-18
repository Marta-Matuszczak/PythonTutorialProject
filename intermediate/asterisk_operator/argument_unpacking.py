def foo(a, b, c):
    print(a, b, c)


my_list = [1, 2, 3]
foo(*my_list)

my_dict = {"a": 1, "b": 2, "c": 3}
print("Dict with * prints keys:")
foo(*my_dict)
print("Dict with ** prints arguments:")
foo(**my_dict)


def foo(*args):
    print(*args)


my_list = [1, 2, 3, 5, 10]
foo(*my_list)


my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
foo(my_dict)
