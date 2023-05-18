def foo():
    global number  # global variable - we can now modify it
    x = number
    number = 3
    print("number inside the function: ", x)


number = 0
foo()
print("number outside the function: ", number)


def foo2():
    number2 = 3  # local variable, does not affect the one outside the function


number2 = 0
foo2()
print("number 2 outside the function: ", number2)
