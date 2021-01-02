import sys
input = sys.stdin.readline
N, S = map(int, input().split())
num_list = list(map(int, input().rstrip().split()))
result = 0
for iter in range(1, 1 << N):
    tot = 0
    for jter in range(N):
        if iter & (1 << jter):
            tot += num_list[jter]
    if tot == S:
        result += 1
print(result)
