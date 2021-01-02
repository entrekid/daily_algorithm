import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
def flip(x, y):
    for iter in range(x, x + 3):
        for jter in range(y, y + 3):
            graph_A[iter][jter] = 1 - graph_A[iter][jter]
graph_A = [list(map(int, input().rstrip())) for _ in range(N)]
graph_B = [list(map(int, input().rstrip())) for _ in range(N)]
cnt = 0
for iter in range(0, N - 2):
    for jter in range(0, M - 2):
        if graph_A[iter][jter] != graph_B[iter][jter]:
            flip(iter, jter)
            cnt += 1
        else:
            continue
for iter in range(0, N):
    for jter in range(0, M):
        if graph_A[iter][jter] != graph_B[iter][jter]:
            print(-1)
            sys.exit(0)
else:
    print(cnt)

