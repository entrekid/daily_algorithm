import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num_list = list(set(list(map(int, input().rstrip().split()))))
num_list.sort()
length = len(num_list)
result = []
ans = []
def go(N, M, index, base):
    if index == M:
        print(*result)
    else:
        for iter in range(base, length):
            result.append(num_list[iter])
            go(N, M, index + 1, iter)
            result.pop()
go(N, M, 0, 0)
