from multiprocessing import Pool
import time


def cube(number):
    return number * number * number


if __name__ == "__main__":

    numbers = range(10)
    pool = Pool()
    # map, apply, join, close
    # will automatically create as many processes as cores on the machine and split iterable into equal size chunks
    # and run this method in parallel
    result = pool.map(cube, numbers)

    pool.close()
    pool.join()

    print(result)
