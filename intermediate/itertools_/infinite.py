from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 17:
        break

"""
a = [1, 2, 3]
for i in cycle(a):
    print(i)
"""

for i in repeat(1, 5):
    print(i)
