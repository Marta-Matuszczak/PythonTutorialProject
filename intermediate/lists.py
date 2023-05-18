# lists are ordered, mutable (changeable) and allow duplicate elements

my_list = [3, "f", "5", "g", 6, 9, 0]
print(type(my_list[0]))
my_new_list = [str(i) for i in my_list]

print(type(my_list[0]))
print(type(my_new_list[0]))
