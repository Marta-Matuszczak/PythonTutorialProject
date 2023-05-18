import sys


def fibonacci(limit):
    # 0 1 1 2 3 5 8 13 21 ...
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(30)
for i in fib:
    print(i)

"""
def fibonacci(limit):
    # 0 1 1 2 3 5 8 13 21 ...
    arr = [0, 1]
    while arr[len(arr) - 1] < limit:
        last = arr[len(arr) - 1]
        arr.append(arr[len(arr) - 2] + last)
    return arr


def fibonacci_generator(limit):
    num1 = 0
    num2 = 1
    yield num1
    yield num2
    while num1 + num2 < limit:
        yield num1 + num2
        temp = num2
        num2 += num1
        num1 = temp


print(fibonacci(20))
print(sys.getsizeof(fibonacci(1000000)))
print(sys.getsizeof(fibonacci_generator(1000000)))


f = fibonacci_generator(20)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
"""
