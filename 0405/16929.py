import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
check = [[False] * M for _ in range(N)]
dist = [[0] * M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cycle = False
def dfs(x, y, color, depth):
    global cycle
    check[x][y] = True
    dist[x][y] = depth
    for iter in range(4):
        new_x = x + dx[iter]
        new_y = y + dy[iter]
        if 0 <= new_x < N and 0 <= new_y < M and graph[new_x][new_y] == color:
            if not check[new_x][new_y]:
                check[new_x][new_y] = True
                dfs(new_x, new_y, color, depth + 1)
            elif check[new_x][new_y]:
                if abs(dist[new_x][new_y] - dist[x][y]) >= 3:
                    cycle = True
                    return


for iter in range(N):
    for jter in range(M):
        if not check[iter][jter]:
            dfs(iter, jter, graph[iter][jter], 0)
            if cycle:
                print("Yes")
                sys.exit(0)
else:
    print("No")

