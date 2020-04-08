N, M = map(int, input().split())
result = []
def go(N, M, index, start):
    if index == M:
        print(*result, sep = " ", end = "\n")
    else:
        for iter in range(start, N + 1):
            result.append(iter)
            go(N, M, index + 1, iter)
            result.pop()
go(N, M, 0, 1)