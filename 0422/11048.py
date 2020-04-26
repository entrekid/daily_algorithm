import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
D = [[0] * (M + 1) for _ in range(N + 1)]

for iter in range(1, N + 1):
    for jter in range(1, M + 1):
        D[iter][jter] = max(D[iter - 1][jter], D[iter - 1][jter - 1], D[iter][jter - 1]) + graph[iter - 1][jter - 1]
print(D[N][M])

