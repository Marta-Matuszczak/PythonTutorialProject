# syntax error (incorrect statement syntax) vs exception
class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, value, message):
        self.value = value
        self.message = message


def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")
    if x < 5:
        raise ValueTooSmallError(x, "Value is too small")


try:
    test_value(2)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.value, e.message)







try:
    a = 3 + "4"
    a = 3 / 0
except ZeroDivisionError as e:
    print("Divide by 0\n" + str(e))
except TypeError as e:
    print("Type error\n" + str(e))
else:
    print("All is fine")
finally:
    print("End of try block, cleaning up...")




#x = -5

#assert (x >= 0), "x is not positive"

"""
if x < 0:
    raise Exception("x should be positive")
"""
