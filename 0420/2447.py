N = int(input())
graph = [[0] * N for _ in range(N)]
def solve(x, y, N):
    for iter in range(3):
        for jter in range(3):
            graph[x + iter * N][y + jter * N] = " "
    else:
        N = N // 3
        solve(N)