my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}
dict_a = {"a": 1, "b": 2}
dict_b = {"c": 3, "d": 4}

print("\nMerge with an asterisk, note that set is unordered")
new_list_asterisk = [*my_tuple, *my_list, *my_set]
print(new_list_asterisk)

print("\nMerge with no asterisk, note that tuple and list became elements, but elements from the set are divided")
new_list_no_asterisk = [my_tuple, my_list, *my_set]
print(new_list_no_asterisk)

print("\nMerge dictionaries with **, use curly brackets: {}")
my_dict = {**dict_a, **dict_b}
print(my_dict)
