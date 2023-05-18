from contextlib import contextmanager  # using this as a decorator

# create a generator
@contextmanager
def open_managed_file(filename):
    f = open(filename, "w")
    try:
        yield f
    finally:
        f.close()


with open_managed_file("custom_notes_func.txt") as file:
    file.write("write something")
