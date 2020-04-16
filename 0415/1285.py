import sys
input = sys.stdin.readline
N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
MAX = 50000
def flip(row, graph1):
    for col in range(N):
        if graph1[row][col] == "H":
            graph1[row][col] = 'T'
        else:
            graph1[row][col] = 'H'
def count(col, graph2):
    HEAD = 0
    for row in range(N):
        if graph2[row][col] == "H":
            HEAD += 1
    TAIL = N - HEAD
    return (HEAD, TAIL)
ans = MAX
for iter in range(1 << N):
    base = graph.copy()
    temp = 0
    for jter in range(N):
        if iter & (1 << jter) != 0:
            flip(jter, base)
    for kter in range(N):
        HEAD, TAIL = count(kter, base)
        if HEAD > TAIL:
            temp += TAIL
        else:
            temp += HEAD
    if ans > temp:
        ans = temp
print(ans)