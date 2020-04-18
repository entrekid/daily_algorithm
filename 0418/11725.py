import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
parent = [-1] * (N + 1)
parent[0] = 0
queue = deque()
queue.append(1)
check = [False] * (N + 1)
check[0] = True
check[1] = True
while queue:
    base = queue.popleft()
    for elem in graph[base]:
        if not check[elem]:
            check[elem] = True
            parent[elem] = base
            queue.append(elem)
for iter in range(2, N + 1):
    print(parent[iter])