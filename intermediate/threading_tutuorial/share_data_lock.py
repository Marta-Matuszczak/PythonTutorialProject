from threading import Thread, Lock
import time

database_value = 0


def increase(lock):
    global database_value

    lock.acquire()  # locks this part to prevent other threads from accessing
    local_copy = database_value

    # processing
    local_copy += 1
    time.sleep(0.1)

    database_value = local_copy
    lock.release()  # always release!!!

    # use lock as a context manager
    with lock:
        local_copy = database_value

        # processing
        local_copy += 1
        time.sleep(0.1)

        database_value = local_copy


if __name__ == "__main__":

    lock = Lock()
    print("start value: ", database_value)

    t1 = Thread(target=increase, args=(lock,))  # args is a tuple
    t2 = Thread(target=increase, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("end value: ", database_value)

    print("end main")

    # result: end value:  4
    # race condition: two threads tried to modify the same variable at the same time