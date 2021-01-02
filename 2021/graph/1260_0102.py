import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for iter in graph:
    iter.sort()

visit_dfs = [False] * (N + 1)
visit_bfs = [False] * (N + 1)

visit_dfs[0] = True
visit_bfs[0] = True


def dfs(start):
    visit_dfs[start] = True
    print(start, end = " ")
    for elem in graph[start]:
        if not visit_dfs[elem]:
            dfs(elem)

dfs(V)
print()

visit_bfs[V] = True
queue = deque()
queue.append(V)

while queue:
    base = queue.popleft()
    print(base, end = " ")
    for elem in graph[base]:
        if not visit_bfs[elem]:
            visit_bfs[elem] = True
            queue.append(elem)



