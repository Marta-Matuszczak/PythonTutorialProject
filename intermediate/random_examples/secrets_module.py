# for security
import secrets

a = secrets.randbelow(10)  # random int, 10 not included
print(a)

b = secrets.randbits(4)  # returns number of bits as int - range from 0 to 15
print(b)

my_list = list("ABCDEFHG")
c = secrets.choice(my_list)
print(c)
