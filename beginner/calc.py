
def raise_to_power(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result *= base_num
    return result


def factorial(num):
    result = 1
    if num == 0:
        return result
    for i in range(1, num + 1):
        result *= i
    return result
