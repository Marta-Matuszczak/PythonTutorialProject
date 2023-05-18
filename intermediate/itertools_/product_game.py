import random
from itertools import product

adjectives = list()
nouns = list()

for i in range(3):
    adj = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    adjectives.append(adj)
    nouns.append(noun)

print("Thank you, enjoy!")

prod_list = list(product(adjectives, nouns))

for i in range(3):
    item = prod_list[random.randrange(len(prod_list))]
    print(item[0] + " " + item[1])
