from timeit import default_timer as timer

# string is ordered, immutable text representation collection data type
# formatting with % or .format() or f-Strings

var1 = 4.552267375435345324
var2 = "Tom"
my_string = "the variable are: {1} and {0:.3f}".format(var1, var2)
print(my_string)


my_string = f"The variables are: {var1*2:.1f} and {var2}"
print(my_string)


"""
var = "Tom"
my_string = "the variable is %s" % var
print(my_string)

# %d - decimal
var = 4.552267375435345324
my_string = "the variable is %d" % var
print(my_string)

# %f - float (6 digits after . by default)
var = 4.552267375435345324
my_string = "the variable is %f" % var
print(my_string)

# %f - float (6 digits after . by default)
var = 4.552267375435345324
my_string = "the variable is %.2f" % var
print(my_string)
"""

a = """I'm happygeh
ioeeng
ioesf"""

"""
b = '     g     '
print(b)
b.strip()
print(b)
b = b.strip()
print(b)
b = "giraffe CAMP"

print(b.upper())
print(b.lower())
print(b.capitalize())
print(b.casefold())
print(b.swapcase())
print(b.startswith("gir"))
print(b.endswith("MP"))
print(b.find("r"))
print(b.find("aff"))
print(b.find("xx"))
print(b.count("f"))
print(b.replace("giraffe", "elephant"))

b = "how are you doing?"
my_list = b.split("a")
print(my_list)
my_list = b.split()
print(my_list)

c = " ".join(my_list)
print(c)
d = "".join(my_list)
print(d)


my_list = ["a"] * 10000000

start = timer()
good_string = ",".join(my_list)
stop = timer()
print(stop - start)
# 0.12314149999999999

start = timer()
bad_string = ""
for i in my_list:
    bad_string += i
stop = timer()
print(stop - start)
# 6.7788492
"""
