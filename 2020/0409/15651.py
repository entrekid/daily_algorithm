N, M = map(int, input().split())
result = []
def go(index, N, M):
    if index == M:
        print(*result, sep = " ", end = "\n")
    else:
        for iter in range(1, N + 1):
            result.append(iter)
            go(index + 1, N, M)
            result.pop()
go(0, N, M)
