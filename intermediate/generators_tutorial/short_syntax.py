# similar to list comprehension, but list comprehension uses [], not ()
import sys

my_generator = (i for i in range(10) if i % 2 == 0)
print(sys.getsizeof(my_generator))
for i in my_generator:
    print(i)

my_list = [i for i in range(10) if i % 2 == 0]
print(sys.getsizeof(my_list))
print(my_list)

my_generator = (i for i in range(10) if i % 2 == 0)
print(list(my_generator))


print()


my_generator = (i for i in range(1000000) if i % 2 == 0)
print(sys.getsizeof(my_generator))

my_list = [i for i in range(1000000) if i % 2 == 0]
print(sys.getsizeof(my_list))
