import math

nums1 = [0, 1, 170, 2, 3, 4, 5, 6, 7, 8, 9]
names = ["Ola", "Kasia", "Marta", "Jakub", "Marek"]
names2 = ["Jakub", "Marek"]
nums2 = [0, 2, 1, 2, 3, 10, 4, 5, 6]
coordinates = (4, 7, 9)
monthConversions = {
    True: "January",
    2: "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May"
}


def print_numbers():
    i = 1
    while i < 10:
        print(i)
        i += 1
    else:
        print("Done")
        print(i)


def max_num(num_list):
    return max(num_list)


def max_num_no_list(n1, n2, n3):
    return max(n1, n2, n3)


def compare_lists(numbers1, numbers2):
    for x in range(len(numbers1)):
        if x == len(numbers2):
            break
        if numbers1[x] > numbers2[x]:
            print(str(numbers1[x]) + " is greater than " + str(numbers2[x]))
        elif numbers1[x] == numbers2[x]:
            print(str(numbers1[x]) + " is equal to " + str(numbers2[x]))
        else:
            print(str(numbers1[x]) + " is less than " + str(numbers2[x]))


