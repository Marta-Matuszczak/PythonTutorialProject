# generators save memory, not time. There is no need to store a list in the memory
# we don't have to wait until all elements have been generated before we start to use them

import functools
from timeit import default_timer
import sys

def time_func(func):
    @functools.wraps(func)
    def wrapper(*args, ** kwargs):
        start = default_timer()
        result = func(*args, **kwargs)
        stop = default_timer()
        print(stop - start)
        return result
    return wrapper


#@time_func
def first_n(n):
    nums = []  # a list to store values
    num = 0
    while num <= n:
        nums.append(num)
        num += 1
    return nums


#@time_func
def first_n_generator(n):  # no list is needed - saves memory
    num = 0
    while num <= n:
        yield num
        num += 1


print(sys.getsizeof(first_n(10)))
print(sys.getsizeof(first_n_generator(10)))
print(first_n_generator(10))
