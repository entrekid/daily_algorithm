import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num_list = list(map(int, input().rstrip().split()))
num_list.sort()
result = []
def go(N, M, index):
    if index == M:
        print(*result, sep = " ", end = "\n")
    else:
        for iter in range(N):
            result.append(num_list[iter])
            go(N, M, index + 1)
            result.pop()
go(N, M, 0)