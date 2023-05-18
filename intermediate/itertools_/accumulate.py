from itertools import accumulate
import operator
from timeit import default_timer

a = [1, 2, 3, 4, 5]
acc = accumulate(a)
print(a)
print(list(acc))
print()
acc = accumulate(a, func=operator.add)
print(a)
print(list(acc))
print()
acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))
print()
acc = accumulate(a, func=operator.sub)
print(a)
print(list(acc))
print()
a = [1, 5, 3, 6, 2]
acc = accumulate(a, func=max)
print(a)
print(list(acc))


def factorial_acc(num):
    start = default_timer()
    if num == 0:
        print(1)
        return
    li = list(range(1, num + 1))
    acc_list = accumulate(li, func=operator.mul)
    var = list(acc_list)[-1]
    stop = default_timer()
    print(stop - start)


# faster
def factorial_mul(num):
    start = default_timer()
    fac = 1
    for i in range(1, num + 1):
        fac *= i
    var = fac
    stop = default_timer()
    print(stop - start)


factorial_acc(10000)
factorial_mul(10000)
