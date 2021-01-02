import sys
input = sys.stdin.readline
T = int(input())
graph = [[0] * 15 for _ in range(15)]
for iter in range(15):
    graph[0][iter] = iter

for floor in range(1, 15):
    for room in range(15):
        for kter in range(room + 1):
            graph[floor][room] += graph[floor - 1][kter]
for _ in range(T):
    k = int(input())
    n = int(input())
    print(graph[k][n])
