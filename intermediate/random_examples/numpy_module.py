import numpy as np

a = np.random.rand(3)  # returns an array
b = np.random.rand(3, 3)  # returns an array 3x3

c = np.random.randint(0, 10, (3, 4))  # 10 is excluded, to get more dimensions use a tuple

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
np.random.shuffle(arr)  # only switches in 1st axis (only rows)
print(arr)

np.random.seed(1)
print(np.random.rand(3, 3))
np.random.seed(1)
print(np.random.rand(3, 3))
