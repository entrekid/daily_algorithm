import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
queue_0 = deque()
queue_1 = deque()
check = [[False] * (M) for _ in range(N)]
dist = [[0] * (M) for _ in range(N)]
graph = [list(map(int, list(input().rstrip()))) for _ in range(N)]
queue_0.append((0, 0))
def inRange(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False
check[0][0] = True
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while queue_0:
    base = queue_0.popleft()
    x, y = base
    for iter in range(4):
        new_x = x + dx[iter]
        new_y = y + dy[iter]
        if inRange(new_x, new_y) and not check[new_x][new_y]:
            check[new_x][new_y] = True
            if graph[new_x][new_y] == 0:
                queue_0.append((new_x, new_y))
                dist[new_x][new_y] = dist[x][y]
            elif graph[new_x][new_y] == 1:
                queue_1.append((new_x, new_y))
                dist[new_x][new_y] = dist[x][y] + 1
    if not queue_0:
        queue_0 = queue_1
        queue_1 = deque()
print(dist[N - 1][M - 1])