from itertools import combinations

word = input()
idx_list = combinations(list(range(1, len(word))), 2)
for n in idx_list:
    print(n)
