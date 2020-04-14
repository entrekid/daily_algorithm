import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
A = [int(input()) for _ in range(N)]
cnt = 0
while K:
    for iter in range(N - 1, -1, -1):
        if A[iter] <= K:
            break
    cnt += 1
    K -= A[iter]
print(cnt)