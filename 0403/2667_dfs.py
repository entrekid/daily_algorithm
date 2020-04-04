import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
cnt = 0
size = int(input())
depth = 0
home_no = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def dfs(x, y):
    global cnt
    check[x][y] = True
    cnt += 1
    for iter in range(4):
        new_x = x + dx[iter]
        new_y = y + dy[iter]
        if 0 <= new_x < size and 0 <= new_y < size and graph[new_x][new_y] == "1"  and not check[new_x][new_y]:
            check[new_x][new_y] = True
            dfs(new_x, new_y)

        
graph = [list(input().rstrip()) for _ in range(size)]
check = [[False] * size for _ in range(size)]
for iter in range(size):
    for jter in range(size):
        if graph[iter][jter] == '0':
            check[iter][jter] = True
        else:
            if graph[iter][jter] == '1' and not check[iter][jter]:
                cnt = 0
                depth += 1
                check[iter][jter] = True
                dfs(iter, jter)
                home_no.append(cnt)

home_no.sort()
print(depth)
print(*home_no, sep = "\n")
