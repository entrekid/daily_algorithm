import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(point, type):
    color[point] = type
    for iter in graph[point]:
        if color[iter] == 0:
            dfs(iter, 3 - type)
test_case = int(input())
for _ in range(test_case):
    V, E = map(int, input().rstrip().split())
    stop = False
    color = [0] * V
    graph = [[] for _ in range(V)]
    for _ in range(E):
        a, b = map(int, input().rstrip().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    for iter in range(V):
        if color[iter] == 0:
            dfs(iter, 1)
    for iter in range(V):
        for elem in graph[iter]:
            if color[iter] == color[elem]:
                stop = True
                break
    if stop:
        print("NO")
    else:
        print("YES")
                
    
    