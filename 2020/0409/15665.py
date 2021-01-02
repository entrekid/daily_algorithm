import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num_list = list(set(list(map(int, input().rstrip().split()))))
num_list.sort()
length = len(num_list)
result = []
def go(length, M , depth):
    if depth == M:
        print(*result)
    else:
        for iter in range(length):
            result.append(num_list[iter])
            go(length, M, depth + 1)
            result.pop()
go(length, M, 0)