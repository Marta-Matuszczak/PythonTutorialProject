# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

d = deque()

d.append(1)
d.append(2)
d.append(3)
print(d)
d.appendleft(5)
print(d)

d.pop()
print(d)
d.popleft()
print(d)

d.extendleft([7, 8, 9])
print(d)
d.rotate(1)
print(d)
d.rotate(1)
print(d)
d.rotate(2)
print(d)
d.rotate(-1)
print(d)
d.clear()
print(d)


"""
# default value of the specified type in case of nonexistent key
default_dict = defaultdict(float)
default_dict["a"] = 1
default_dict["b"] = 2
print(default_dict["f"])
"""

"""
# since pthon 3.7 ordered is the default for normal dictionaries
my_dict = dict()
my_dict["a"] = 1
my_dict["c"] = 2
my_dict["b"] = 3
print(my_dict)

ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["c"] = 2
ordered_dict["b"] = 3
print(ordered_dict)
"""

"""
Point = namedtuple("Point", "x,y")
point = Point(2, 6)
print(point)
print(type(point))
print(point.x, point.y)

Rectangle = namedtuple("RRR", "width,height,colour")
rect = Rectangle(2, 6, "brown")
print(rect.width, rect.height, rect.colour)
a, b, c = rect
print(c)
"""

"""
a = "hhhhhhhhhhhh222222222222228882gd278dq7dhiqhd8yr83rywirghriwqhqo2"
my_counter = Counter(a)
print(my_counter)
print(my_counter.elements())
print(list(my_counter.elements()))
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print()
print(my_counter.most_common())
print(my_counter.most_common(2))
print(my_counter.most_common(1))
print(my_counter.most_common()[0])
print(my_counter.most_common()[0][0])
print(my_counter.most_common()[0][1])
print(Counter(a).most_common()[-1])
"""
