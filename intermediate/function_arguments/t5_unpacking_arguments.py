def foo(a, b, c):
    print(a, b, c)


my_list = [0, 1, 2]
foo(*my_list)  # * unpacks the list (length of the container must match the number of parameters)

my_tuple = (1, 2, 3)
foo(*my_tuple)  # works with tuples (length of the container must match the number of parameters)

my_dict = {"a": 2, "b": 3, "c": 4}
foo(**my_dict)  # keys must match the names of parameters, length must match
