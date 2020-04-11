N, K = map(int, input().split())
graph = [[0] * 1001 for _ in range(1001)]
for iter in range(1, 1001):
    graph[iter][iter] = 1
    graph[iter][0] = 1
for row in range(2, 1001):
    for col in range(1, row + 1):
        graph[row][col] = (graph[row - 1][col - 1] + graph[row - 1][col]) % 10007
print(graph[N][K] % 10007)
