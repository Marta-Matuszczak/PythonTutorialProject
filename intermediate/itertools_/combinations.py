from itertools import combinations, combinations_with_replacement

a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

family = ["mom", "dad", "daughter", "son"]
comb = combinations(family, 2)
print(list(comb))
