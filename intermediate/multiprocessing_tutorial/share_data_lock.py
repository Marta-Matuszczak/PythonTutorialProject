from multiprocessing import Process, Value, Array, Lock
import os
import time


def add_100(number, lock):
    for _ in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1


def add_100_arr(numbers, lock):
    for _ in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1


if __name__ == "__main__":

    lock = Lock()
    shared_number = Value("i", 0)
    print("number at the beginning is: ", shared_number.value)

    p1 = Process(target=add_100, args=(shared_number, lock))
    p2 = Process(target=add_100, args=(shared_number, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("number at the end os: ", shared_number.value)

    shared_array = Array("d", [0.0, 100.0, 200.0])
    print("array at the beginning is: ", shared_array[:])

    p1 = Process(target=add_100_arr, args=(shared_array, lock))
    p2 = Process(target=add_100_arr, args=(shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("array at the end is: ", shared_array[:])

