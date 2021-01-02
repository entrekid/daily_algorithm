import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
group = [[0] * N for _ in range(N)]
group_no = 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def inRange(x, y):
    return 0 <= x < N and 0 <= y < N
def bfs(x, y, group_no):
    queue = deque()
    queue.append((x, y))
    group[x][y] = group_no
    check[x][y] = True
    while queue:
        base = queue.popleft()
        x, y = base
        for iter in range(4):
            new_x = x + dx[iter]
            new_y = y + dy[iter]
            if inRange(new_x, new_y) and group[new_x][new_y] == 0 and graph[new_x][new_y] == 1:
                group[new_x][new_y] = group_no
                check[new_x][new_y] = True
                queue.append((new_x, new_y))
check = [[False] * N for _ in range(N)]
for iter in range(N):
    for jter in range(N):
        if not check[iter][jter] and graph[iter][jter] == 1:
            bfs(iter, jter, group_no)
            group_no += 1

ans = 1000000
for group_idx in range(1, group_no):
    dist = [[-1] * N for _ in range(N)]
    queue = deque()
    for iter in range(N):
        for jter in range(N):
            if group[iter][jter] == group_idx:
                dist[iter][jter] = 0
                queue.append((iter, jter))
    while queue:
        base = queue.popleft()
        x, y = base
        for iter in range(4):
            nx = x + dx[iter]
            ny = y + dy[iter]
            if inRange(nx, ny) and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    for iter in range(N):
        for jter in range(N):
            if graph[iter][jter] == 1 and graph[iter][jter] != group_idx and dist[iter][jter] != 0:
                if ans > dist[iter][jter] - 1:
                    ans = dist[iter][jter] - 1

print(ans)