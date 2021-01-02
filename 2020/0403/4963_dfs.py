import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
def dfs(x, y):
    check[x][y] = True
    for iter in range(8):
        new_x = x + dx[iter]
        new_y = y + dy[iter]
        if 0 <= new_x < H and 0 <= new_y < W and graph[new_x][new_y] == 1 and not check[new_x][new_y]:
            check[new_x][new_y] = True
            dfs(new_x, new_y)
            
while True:
    cnt = 0
    W, H = map(int, input().split())
    check = [[False] * W for _ in range(H)]
    if W == 0 and H == 0:
        break
    graph = [list(map(int, input().rstrip().split())) for _ in range(H)]
    for iter in range(H):
        for jter in range(W):
            if graph[iter][jter] == 0:
                check[iter][jter] = True
            elif graph[iter][jter] == 1 and not check[iter][jter]:
                check[iter][jter] = True
                dfs(iter, jter)
                cnt += 1

    print(cnt)
