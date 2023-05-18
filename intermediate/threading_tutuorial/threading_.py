from threading import Thread


def square_numbers():
    for j in range(10):
        j * j


if __name__ == "__main__":
    threads = []
    num_threads = 10

    # create threads
    for i in range(num_threads):
        t = Thread(target=square_numbers())
        threads.append(t)

    # start threads
    for t in threads:
        t.start()

    # join threads - wait for them to complete
    for t in threads:
        t.join()

    print("end main")
