# call by object
# call by object reference

def foo1(x):
    x = 5


var = 10  # integer - immutable type and can't be changed inside a function
foo1(var)
print(var)


def foo2(a_list):
    a_list.append(5)


my_list = []  # list is a mutable type and can be modified inside a function
print(my_list)
foo2(my_list)
print(my_list)


def foo3(a_list):
    a_list[0] = 1


foo3(my_list)  # immutable int within a mutable list can be modified inside a function
print(my_list)


def foo4(a_list):
    a_list = [100, 200, 300]  # rebinding a reference - a_list is now a local variable, so the ane passed as an
    # argument won't be changed
    a_list.append(70)


foo4(my_list)
print(my_list)


def foo5(a_list):
    a_list = a_list + [100, 200, 300]  # this creates a local variable with the same name


foo5(my_list)
print("a_list = a_list + [100, 200, 300]\n", my_list)


def foo6(a_list):
    a_list += [100, 200, 300]  # this adds elements to the global variable, not creating a local one


foo6(my_list)
print("a_list += [100, 200, 300]\n", my_list)
