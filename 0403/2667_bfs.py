import sys
from collections import deque
sys.setrecursionlimit(10 **6)
input = sys.stdin.readline

no = 0
cnt = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
home_no = []
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    cnt = 1
    while queue:
        base_x, base_y = queue.popleft()
        check[base_x][base_y] = True
        for iter in range(4):
            new_x = base_x + dx[iter]
            new_y = base_y + dy[iter]
            if 0 <= new_x < size and 0 <= new_y < size and not check[new_x][new_y] and graph[new_x][new_y] == "1":
                queue.append((new_x, new_y))
                check[new_x][new_y] = True
                cnt += 1
    return cnt
size = int(input())
graph = [list(input().rstrip()) for _ in range(size)]
check = [[False] * size for _ in range(size)]
for iter in range(size):
    for jter in range(size):
        if graph[iter][jter] == "0":
            check[iter][jter] = True
        else:
            if graph[iter][jter] == "1" and not check[iter][jter]:
                check[iter][jter] = True
                no += 1
                home_no.append(bfs(iter, jter))
home_no.sort()
print(no)
print(*home_no, sep = "\n")