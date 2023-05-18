
try:
    value = 10/0
except ZeroDivisionError as err:
    print(err)

try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError as err:
    print(err)
