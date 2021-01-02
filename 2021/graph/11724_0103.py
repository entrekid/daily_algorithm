import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visit = [False] * (N + 1)
visit[0] = True

def dfs(elem):
    visit[elem] = True
    for i in graph[elem]:
        if not visit[i]:
            dfs(i)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for elem in graph:
    elem.sort()

component = 0
for i in range(1, N + 1):
    if not visit[i]:
        component += 1
        dfs(i) 

print(component)

