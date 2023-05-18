from timeit import default_timer


def start_end_decorator(func):

    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper


def time_something(func):
    def wrapper():
        start = default_timer()
        func()
        end = default_timer()
        print("Time: " + str(end - start))
    return wrapper


@time_something
@start_end_decorator
def print_name():
    print("Max")


print_name()


