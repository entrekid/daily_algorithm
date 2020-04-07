import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(start, depth):
    dist[start] = depth
    check[start] = True
    for elem in graph[start]:
        if not check[elem]:
            check[elem] = True
            parent[elem] = start
            dfs(elem, depth + 1)
        elif check[elem]:
            print(dist)
            print(dist[elem], dist[start])
            if abs(dist[elem] - dist[start]) >= 3:
                
                # 여기서 cycle 정리
                parent[elem] = start
                cy_start = elem
                cy_end = start
                base = start
                cycle[cy_start] = True
                while base != cy_start:
                    cycle[base] = True
                    base = parent[base]
                    print(cycle, base)

N = int(input())
graph = [[] for _ in range(N)]
dist = [0] * N
check = [False] * N
parent = [0] * N
cycle = [False] * N
for _ in range(N):
    a, b = map(int, input().rstrip().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
for iter in range(N):
    graph[iter].sort()
dfs(0, 0)
