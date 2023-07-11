from itertools import permutations

S, k = input().split()
k = int(k)

permutations_list = list(permutations(sorted(S), k))
for item in permutations_list:
    print("".join(item))
