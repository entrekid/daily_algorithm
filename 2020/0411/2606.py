import sys
input = sys.stdin.readline
N = int(input())
connect = int(input())
graph = [[] for _ in range(N)]
for _ in range(connect):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

check = [False] * N
def dfs(start):
    check[start] = True
    for elem in graph[start]:
        if check[elem]:
            continue
        check[elem] = True
        dfs(elem)
dfs(0)
print(sum(check) - 1)