import sys
input = sys.stdin.readline
test_case = int(input())
def jump(x, y):
    if x >= n or y >= n:
        return False
    if x == n - 1 and y == n - 1:
        return True
    if check[x][y] != -1:
        return check[x][y]
    ret = jump(x + graph[x][y], y) or jump(x, y + graph[x][y])
    check[x][y] = ret
    return ret
for _ in range(test_case):
    n = int(input())
    check = [[-1] * n for _ in range(n)]
    graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
    print('YES' if jump(0, 0) else 'NO')