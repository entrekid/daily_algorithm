import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
T = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def dfs(x, y):
    for iter in range(4):
        new_x = x + dx[iter]
        new_y = y + dy[iter]
        if 0 <= new_x < M and 0 <= new_y < N and not check[new_x][new_y] and graph[new_x][new_y]:
            check[new_x][new_y] = True
            dfs(new_x, new_y)

for _ in range(T):
    M, N, K = map(int, input().rstrip().split())
    graph = [[0] * N for _ in range(M)]
    check = [[False] * N for _ in range(M)]
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a][b] = 1
    cnt = 0
    for iter in range(N):
        for jter in range(M):
            if check[jter][iter]:
                continue
            elif not check[jter][iter] and graph[jter][iter]:
                check[jter][iter] = True
                cnt += 1
                dfs(jter, iter)
    print(cnt)

    