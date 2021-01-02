import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, start = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

check1 = [False] * (N + 1)
check1[0] = True
def dfs(start):
    check1[start] = True
    print(start, end = " ")
    for iter in range(1, N + 1):
        if graph[start][iter] and not check1[iter]:
            dfs(iter)

dfs(start)
print()

check2 = [False] * (N + 1)
check2[0] = True
def bfs(start):
    check2[start] = True
    queue = deque()
    queue.append(start)
    while queue:
        basis = queue.popleft()
        print(basis, end = " ")
        for iter in range(N + 1):
            if graph[basis][iter] and not check2[iter]:
                check2[iter] = True
                queue.append(iter)
bfs(start)
print()