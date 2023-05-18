from threading import Thread
import time

database_value = 0


def increase():
    global database_value

    local_copy = database_value

    # processing
    local_copy += 1
    time.sleep(0.1)  # because we use sleep, program can switch to the other thread and use the waiting time

    database_value = local_copy


if __name__ == "__main__":

    print("start value: ", database_value)

    t1 = Thread(target=increase)
    t2 = Thread(target=increase)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("end value: ", database_value)

    print("end main")

    # result: end value:  1
    # race condition: two threads tried to modify the same variable at the same time