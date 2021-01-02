import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
base = map(int, input().rstrip().split())
base = list(elem - 1 for elem in base)
order = [0] * N
for i in range(N):
    order[base[i]] = i
for iter in range(N):
    graph[iter].sort(key = lambda x : order[x])
check = [False] * N
queue = deque()
bfs_order = []
queue.append(0)
check[0] = True
while queue:
    basis = queue.popleft()
    bfs_order.append(basis)
    for elem in graph[basis]:
        if not check[elem]:
            check[elem] = True
            queue.append(elem)
ans = True
for iter in range(N):
    if base[iter] != bfs_order[iter]:
        ans = False
        break
print(1 if ans else 0)