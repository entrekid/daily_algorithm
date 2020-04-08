import sys
input = sys.stdin.readline
N, M = map(int, input().split())
check = [False] * (N + 1)
check[0] = True
result = []
def go(N, M, depth, start):
    if depth == M:
        print(*result, sep = " ", end = "\n")
    else:
        for iter in range(start, N + 1):
            if check[iter]:
                continue
            else:
                check[iter] = True
                result.append(iter)
                go(N, M, depth + 1, iter)
                check[iter] = False
                result.pop()
go(N, M, 0, 1)