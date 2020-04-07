import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
"""
일단 dfs를 돌리면 전부 다 지나갈 수 있다.

dfs를 돌리면서 싸이클의 시작점과 끝점을 찾는다
만나면 부모노드를 쭉 거슬러서 간다. 시작점이 될 때까지
그리고 해당 노드들 cycle 표시를 모두 한다
그리고나서 각 점에서 cycle 점까지 모두 dist를 계산(dfs를 돌려서)
종료
"""
n = int(input())
graph = [[] for _ in range(n)]
ans = [0] * n
parent = [0] * n
check = [False] * n
cycle = [False] * n
dist = [0] * n
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
for iter in range(n):
    graph[iter].sort()
def dfs(depth, start):
    check[start] = True
    dist[start] = depth
    for elem in graph[start]:
        if not check[elem]:
            check[elem] = True
            parent[elem] = start
            dfs(depth + 1, elem)
        elif check[elem]:
            if abs(dist[elem] - dist[start]) >= 3:
                '''여기까지 cycle 시작점과 끝점 구함
                    start에서 시작해서 쭉 거슬러 올라가서 elem까지 모두
                    cycle = True 작업을 진행하면 됨
                '''
                cycle[start] = True
                parent[elem] = start
                base = parent[start]
                while base != start:
                    cycle[base] = True
                    base = parent[base]
dfs(0, 0)
ret = 0
def dfs2(start):
    global ret
    check2[start] = True
    for elem in graph[start]:
        if cycle[elem]:
            ret = abs(dist[elem] - dist[start])
            return
        else:
            dfs2(elem)
            
for iter in range(n):
    if cycle[iter]:
        ans[iter] = 0
    else:
        check2 = [False] * n
        dfs2(iter)
        if ret:
            ans[iter] = ret

print(*ans, sep = " ", end = "\n")