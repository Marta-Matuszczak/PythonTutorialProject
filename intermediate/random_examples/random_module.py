import random

a = random.random()  # returns float
b = random.uniform(1, 10)  # returns float
c = random.randint(1, 10)  # returns int, includes 10
d = random.randrange(1, 10)  # returns int, does not include 10
e = random.normalvariate(0, 1)  # rozkład normalny

my_list = list("ABCDEFGH")
f = random.choice(my_list)  # random element from a list
g = random.sample(my_list, 3)  # pick a number of unique elements from a list
h = random.choices(my_list, k=3)  # pick a number of elements from a list, element can be picked more times
print(h)

random.shuffle(my_list)
print(my_list)
