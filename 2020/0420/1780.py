import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
cnt = [0] * 3
def check(x, y, N):
    for iter in range(N):
        for jter in range(N):
            if graph[x][y] != graph[x + iter][y + jter]:
                return False
    return True
def solve(x, y, N):
    if check(x, y, N):
        cnt[graph[x][y] + 1] += 1
        return
    else:
        M = N // 3
        for iter in range(3):
            for jter in range(3):
                solve(x + iter*M, y + jter*M, M)
solve(0, 0, N)
print(*cnt, sep = "\n", end = "\n")