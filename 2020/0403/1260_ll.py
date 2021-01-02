import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N, M, start = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for iter in range(1, N + 1):
    graph[iter].sort()

check1 = [False] * (N + 1)
check1[0] = True
def dfs(start):
    check1[start] = True
    print(start, end = ' ')
    for iter in graph[start]:
        if not check1[iter]:
            dfs(iter)
dfs(start)
print( )

check2 = [False] * (N + 1)
check2[0] = True
def bfs(start):
    queue = deque()
    queue.append(start)
    check2[start] = True
    while queue:
        basis = queue.popleft()
        print(basis, end = " ")
        for elem in graph[basis]:
            if not check2[elem]:
                check2[elem] = True
                queue.append(elem)
bfs(start)
print()