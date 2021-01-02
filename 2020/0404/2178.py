import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0
def bfs(N, M):
    queue = deque()
    check[0][0] = True
    queue.append((0, 0))
    while queue:
        base_x, base_y= queue.popleft()

        if base_x == N - 1 and base_y == M - 1:
            return graph[base_x][base_y]
        check[base_x][base_y] = True
        for iter in range(4):
            new_x = base_x + dx[iter]
            new_y = base_y + dy[iter]
            if 0 <= new_x < N and 0 <= new_y < M and graph[new_x][new_y] == 1 and not check[new_x][new_y]:
                check[new_x][new_y] = True
                queue.append((new_x, new_y))
                graph[new_x][new_y] = graph[base_x][base_y] + 1
N, M = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(N)]
check = [[False] * M for _ in range(N)]
print(bfs(N, M))