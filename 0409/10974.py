from itertools import permutations
num = int(input())
for perm in permutations(range(1, num + 1)):
    print(*perm)