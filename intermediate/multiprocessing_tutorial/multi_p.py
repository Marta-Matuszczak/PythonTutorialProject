from multiprocessing import Process
import os
import time


def square_numbers():
    for j in range(100):
        j * j
        time.sleep(0.01)


if __name__ == "__main__":

    processes = []
    num_processes = os.cpu_count()  # number of CPUs on the machine, usually a good choice for the number of processes

    # create processes and assign a function for each process
    for i in range(num_processes):
        p = Process(target=square_numbers())
        processes.append(p)

    # start all processes
    for p in processes:
        p.start()

    # join (wait for the process to finish and while waiting, blocking the main thread)
    for p in processes:
        p.join()

    print("end main")
