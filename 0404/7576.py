import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
N, M = map(int, input().split())
check = [[False] * N for _ in range(M)]
def bfs(no_list):
    queue = deque()
    for elem in no_list:
        queue.append(elem)
        check[elem[0]][elem[1]] = True
    while queue:
        base_x, base_y = queue.popleft()
        for iter in range(4):
            new_x = base_x + dx[iter]
            new_y = base_y + dy[iter]
            if 0 <= new_x < M and 0 <= new_y < N and graph[new_x][new_y] != 1 and graph[new_x][new_y] != -1 and not check[new_x][new_y]:
                check[new_x][new_y] = True
                graph[new_x][new_y] = graph[base_x][base_y] + 1
                queue.append((new_x, new_y))


graph = [list(map(int, input().rstrip().split())) for _ in range(M)]
no_list = []
for iter in range(M):
    for jter in range(N):
        if graph[iter][jter] == 1:
            no_list.append((iter, jter))
bfs(no_list)
# map이 완성
"""
완성 되었을 때 여전히 0이 남아있다면 -1을 출력해야 함
"""
ans = []
ret = 0
stop = False
for iter in range(M):
    if 0 in graph[iter]:
        stop = True
        break
    else:    
        ans.append(max(graph[iter]))
if stop:
    print(-1)
else:    
    print(max(ans) - 1)