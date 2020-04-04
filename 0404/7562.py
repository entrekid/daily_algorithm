import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def bfs(x_start, y_start, x_end, y_end, graph):
    queue = deque()
    queue.append((x_start, y_start))
    cnt= 0
    while queue:
        x_base, y_base = queue.popleft()
        if x_base == x_end and y_base == y_end:
            return cnt
        cnt = graph[x_base][y_base]
        for iter in range(8):
            new_x = x_base + dx[iter]
            new_y = y_base + dy[iter]
            if 0 <= new_x < size and 0 <= new_y < size and graph[new_x][new_y] == 0:
                graph[new_x][new_y] = graph[x_base][y_base] + 1 
                queue.append((new_x, new_y))
test_case = int(input())
dx = [1, 1, 2, 2, -2, -2, -1, -1]
dy = [2, -2, 1, -1, 1, -1, 2, -2]
for _ in range(test_case):
    size = int(input())
    graph = [[0] * size for _ in range(size)]
    x_start, y_start = map(int, input().split())
    x_end, y_end = map(int, input().split())
    print(bfs(x_start, y_start, x_end, y_end, graph))