from itertools import product
N, M = map(int, input().split())
for num in product(range(1, N + 1), repeat = M):
    print(*num, sep = " ", end = "\n")