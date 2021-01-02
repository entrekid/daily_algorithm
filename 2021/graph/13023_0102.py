import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

check = [False] * N 
cnt = 0
def dfs(depth, start):
    global cnt
    if depth == 4:
        cnt += 1
        return
    else:
        check[start] = True
        for elem in graph[start]:
            if not check[elem]:
                check[elem] = True
                dfs(depth + 1, elem)
                check[elem] = False
        check[start] = False
    
for iter in range(N):
    dfs(0, iter)
    if cnt:
        break

if cnt:
    print(1)
else:
    print(0)