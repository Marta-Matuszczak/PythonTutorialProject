from threading import Lock
lock = Lock()

lock.acquire()
# do something...
lock.release()


with lock:
    # do something
    pass
