import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
w = [list(map(int, input().rstrip().split())) for _ in range(N)]
MAX = 100000000
ans = MAX

def weight(num_list):
    global N
    global MAX
    ret = 0
    for iter in range(N - 1):
        if not w[num_list[iter]][num_list[iter + 1]]:
            return MAX
        else:
            ret += w[num_list[iter]][num_list[iter + 1]]
    if not w[num_list[iter + 1]][num_list[0]]:
        return MAX
    else:
        ret += w[num_list[iter + 1]][num_list[0]]
        return ret
perm_list = permutations(range(N))
base = 0
for perm in perm_list:
    if base != perm[0]:
        break
    temp = weight(perm)
    if ans > temp:
        ans = temp
print(ans)