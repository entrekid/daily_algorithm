import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
cnt = 0
def check(x, y, N):
    for iter in range(N):
        for jter in range(N):
            if graph[x][y] != graph[x + iter][y + jter]:
                return False
    return True
def solve(x, y, N):
    global cnt
    N = N // 2
    if N == 0:
        return
    for iter in range(2):
        for jter in range(2):
            if check(x + iter * (N), y + jter * (N), N):
                cnt += 1
            else:
                solve(x + iter * N, y + iter * N, N)
solve(0, 0, N)
print(cnt)