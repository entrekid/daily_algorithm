import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
d = [[-1] * (M) for _ in range(N)]
d[0][0] = graph[0][0]
def inRange(x, y):
    return 0 <= x < N and 0 <= y < M
def solve(x, y):
    if x < 0 or y < 0:
        return 0
    if d[x][y] != -1:
        return d[x][y]
    check1 = inRange(x - 1, y)
    check2 = inRange(x - 1, y - 1)
    check3 = inRange(x, y - 1)
    check_list = []
    if check1:
        check_list.append(solve(x - 1, y))
    if check2:
        check_list.append(solve(x, y - 1))
    if check3:
        check_list.append(solve(x - 1, y - 1))
    d[x][y] = max(check_list) + graph[x][y]
    return d[x][y]
print(solve(N - 1, M - 1))