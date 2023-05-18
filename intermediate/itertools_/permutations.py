from itertools import permutations

a = [1, 2, 3]
perm = permutations(a)
print(list(perm))

perm2 = permutations(a, 2)
print(list(perm2))

word = "list"
word_perm = permutations(word)
words_list = list(word_perm)
new_list = ["".join(list(w)) for w in words_list]
print(new_list)
