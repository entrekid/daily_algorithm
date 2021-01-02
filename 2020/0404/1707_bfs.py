import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
from collections import deque

test_case = int(input())
def bfs(code, start):
    queue = deque()
    queue.append(start)
    color[start] = code
    while queue:
        base = queue.popleft()
        for elem in graph[base]:
            if color[elem] == 0:
                code = color[base]
                color[elem] = 3 - code
                queue.append(elem)

for _ in range(test_case):
    V, E = map(int, input().rstrip().split())
    color = [0] * V
    graph = [[] for _ in range(V)]
    stop = False
    for _ in range(E):
        a, b = map(int, input().rstrip().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    for iter in range(V):
        if color[iter] == 0:
            bfs(1, iter)
    for iter in range(V):
        for elem in graph[iter]:
            if color[iter] == color[elem]:
                stop = True
                break
    print("YES" if not stop else "NO")