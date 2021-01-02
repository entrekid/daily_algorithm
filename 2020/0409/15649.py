import sys
input = sys.stdin.readline
N, M = map(int, input().split())
result = []
check = [False] * (N + 1)
check[0] = True
def go(N, M, depth):
    if depth == M:
       print(*result, sep = " ", end = "\n")
    for iter in range(1, N + 1):
        if check[iter]:
            continue
        check[iter] = True
        result.append(iter)
        go(N, M, depth + 1)
        check[iter] = False
        result.pop()
go(N, M , 0)