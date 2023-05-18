class ManagedFile:
    def __init__(self, filename):
        print("init")
        self.filename = filename

    def __enter__(self):
        print("enter")
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print("Exception has been handled")
        #print("exc:", exc_type, exc_val, exc_tb)
        print("exit")
        return True  # to continue after exception


with ManagedFile("custom_notes.txt") as file:
    print("do something")
    file.write("Notes created using custom context manager")
    file.somemethod()

print("continuing")
