import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().rstrip().split()))
A.sort()
ans = 0
for iter in range(N):
    temp = 0
    for jter in range(iter + 1):
        temp += A[jter]
    ans += temp
print(ans)