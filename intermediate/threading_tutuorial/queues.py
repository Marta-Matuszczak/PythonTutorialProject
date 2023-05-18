from threading import Thread, Lock, current_thread
from queue import Queue
import time

# queue - FIFO


def worker(q, lock):
    while True:
        value = q.get()

        # processing..
        with lock:  # prevents multiple threads from writing in the same line
            print(f"in {current_thread().name} got {value}")
            q.task_done()


if __name__ == "__main__":

    q = Queue()

    num_threads = 10
    lock = Lock()
    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True  # background thread that will die when the main thread dies (while True will stop)
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()

    print("end main")


"""
    q = Queue()

    q.put(1)
    q.put(2)
    q.put(3)
    # 3 2 1 --> front
    first = q.get()  # gets AND removes the first item
    print(first)

    print(q.empty())

    q.task_done()
    q.join()

    print("end main")
"""
