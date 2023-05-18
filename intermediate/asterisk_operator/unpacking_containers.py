my_list = [1, 2, 3]
my_tuple = (1, 2, 3, 4, 5, 6)
my_set = {7, 8, 9, 10, 11, 12}

*beginning, last = my_list
print(beginning)
print(last)


*beginning_from_set, last_second, last = my_set
print("Always unpacks to list, even from sets or tuples: ", beginning_from_set, last_second, last)

first, *middle, last = my_tuple
print(first, middle, last)

