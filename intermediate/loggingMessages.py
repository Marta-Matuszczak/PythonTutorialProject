import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')

try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    print("Caught exception")
    logging.error(e, exc_info=True)
    print("Logged an error")

print("Still working")
