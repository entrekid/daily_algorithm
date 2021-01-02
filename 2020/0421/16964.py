import sys
input = sys.stdin.readline
N = int(input())
check = [False] * N
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
compare = map(int, input().rstrip().split())
compare = list(elem - 1 for elem in compare)
order = [0] * N
for iter in range(N):
    order[compare[iter]] = iter
for iter in range(N):
    graph[iter].sort(key = lambda x : order[x])

dfs_order = []
def dfs(x):
    if check[x]:
        return
    dfs_order.append(x)
    check[x] = True
    for y in graph[x]:
        dfs(y)
dfs(0)
ans = True
for iter in range(N):
    if dfs_order[iter] != compare[iter]:
        ans = False
        break
print(1 if ans else 0)