import sys
input = sys.stdin.readline
from itertools import permutations
num = int(input())
a_list = list(map(int, input().rstrip().split()))
b_list = list(map(int, input().rstrip().split()))
a_list.sort(reverse = True)
b_list.sort()
ans = 0
for iter in range(num):
    ans += (a_list[iter] * b_list[iter])
print(ans)