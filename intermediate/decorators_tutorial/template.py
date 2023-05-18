import functools



def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something...
        result = func(*args, **kwargs)
        # Do something...
        return result
    return wrapper


@my_decorator
def my_function(x):
    print(x)


