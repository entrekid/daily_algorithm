import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
W, H = map(int, input().split())
graph = [ list(input().rstrip().split()) for _ in range(H)]
check = [[False] * W for _ in range(H)]
for col in range(W):
    for row in range(H):
        if graph[row][col] == '0':
            check[row][col] = True
        else:
            if graph[row][col] == '1' and not check[row][col]:
                check[row][col] = True