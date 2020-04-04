import sys
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(x, y):
    queue = deque()
    check[x][y] = True
    queue.append((x, y))
    while queue:
        base_x, base_y = queue.popleft()
        check[base_x][base_y] = True
        for iter in range(8):
            new_x = base_x + dx[iter]
            new_y = base_y + dy[iter]
            if 0 <= new_x < row and 0 <= new_y < col and graph[new_x][new_y] == 1 and not check[new_x][new_y]:
                check[new_x][new_y] = True
                queue.append((new_x, new_y))
                
while True:
    col, row = map(int, input().split())
    cnt = 0
    check = [[False] * col for _ in range(row)]

    if row == 0 and col == 0:
        break
    graph = [list(map(int, input().rstrip().split())) for _ in range(row)]
    for iter in range(row):
        for jter in range(col):
            if graph[iter][jter] == 0:
                check[iter][jter] = True
            elif graph[iter][jter] == 1 and not check[iter][jter]:
                check[iter][jter] = True
                bfs(iter, jter)
                cnt += 1
    print(cnt)