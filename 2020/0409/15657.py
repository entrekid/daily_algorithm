import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num_list = list(map(int, input().rstrip().split()))
num_list.sort()
result = []
def go(N, M, index, base):
    if index == M:
        print(*result, sep = " ", end = "\n")
    else:
        for iter in range(base, N):
            result.append(num_list[iter])
            go(N, M, index + 1, iter)
            result.pop()
go(N, M, 0, 0)
