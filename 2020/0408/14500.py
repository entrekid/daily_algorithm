import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
ans = -1
for iter in range(N):
    for jter in range(M):
        # case 1
        if jter + 3 < M:
            temp = graph[iter][jter] + graph[iter][jter + 1] + graph[iter][jter + 2] + graph[iter][jter + 3]
            if ans < temp:
                ans = temp
        # case 2
        if iter + 3 < N:
            temp = graph[iter][jter] + graph[iter + 1][jter] + graph[iter + 2][jter] + graph[iter + 3][jter]
            if ans < temp:
                    ans = temp
        # case 3
        if iter + 1  < N and jter + 1 < M:
            temp = graph[iter][jter] + graph[iter][jter + 1] + graph[iter + 1][jter] + graph[iter + 1][jter + 1]
            if ans < temp:
                ans = temp
        # case 4
        if iter + 1 < N and jter + 2 < M:
            temp = graph[iter][jter] + graph[iter][jter + 1] + graph[iter][jter + 2] + graph[iter + 1][jter]
            if ans < temp:
                ans = temp
        # case 5
        if iter + 3 < N and jter + 1 < M:
            temp = graph[iter][jter] + graph[iter + 1][jter] + graph[iter + 2][jter] + graph[iter + 2][jter + 1]
            if ans < temp:
                ans = temp
        # case 6
        if iter + 2 < N and jter + 1 < M:
            temp = graph[iter][jter] + graph[iter + 1][jter] + graph[iter + 2][jter] + graph[iter][jter + 1]
            if ans < temp:
                ans = temp
        # case 7
        if iter + 2 < N and 0 <= jter - 1:
            temp = graph[iter][jter] + graph[iter + 1][jter] + graph[iter + 2][jter] + graph[iter + 2][jter - 1]
            if ans < temp:
                ans = temp
        # case 8
        if iter + 2 < N and jter + 1 < M:
            temp = graph[iter][jter] + graph[iter][jter + 1] + graph[iter + 1][jter + 1] + graph[iter + 2][jter + 1]
            if ans < temp:
                ans = temp
        # case 9
        if 0 <= iter - 1 and jter + 2 < M:
            temp = graph[iter][jter] + graph[iter][jter + 1] + graph[iter][jter + 2] + graph[iter - 1][jter + 2]
            if ans < temp:
                ans = temp
        # case 10
        if iter + 1 < N and jter + 2 < M:
            temp = graph[iter][jter] + graph[iter + 1][jter] + graph[iter + 1][jter + 1] + graph[iter + 1][jter + 2]
            if ans < temp:
                ans = temp
        # case 11
        if iter + 1 < N and jter + 2 < M:
            temp = graph[iter][jter] + graph[iter][jter + 1] + graph[iter][jter + 2] + graph[iter + 1][jter + 2]
            if ans < temp:
                ans = temp
        # case 12
        if 0 <= iter - 1 and jter + 2 < M:
            temp = graph[iter][jter] + graph[iter][jter + 1] + graph[iter][jter + 2] + graph[iter - 1][jter + 1]
            if ans < temp:
                ans = temp
        # case 13
        if iter + 1 < N and jter + 2 < M:
            temp = graph[iter][jter] + graph[iter][jter + 1] + graph[iter][jter + 2] + graph[iter + 1][jter + 1]
            if ans < temp:
                ans = temp
        # case 14
        if 0 <= iter - 1 and iter + 1 < N and jter + 1 < M:
            temp = graph[iter][jter] + graph[iter][jter + 1] + graph[iter - 1][jter + 1] + graph[iter + 1][jter  + 1]
            if ans < temp:
                ans = temp
        # case 15
        if iter + 2 < N and jter + 1 < M:
            temp = graph[iter][jter] + graph[iter + 1][jter] + graph[iter + 2][jter] + graph[iter + 1][jter + 1]
            if ans < temp:
                ans = temp
        # case 16
        if iter + 2 < N and jter + 1 < M:
            temp = graph[iter][jter] + graph[iter + 1][jter] + graph[iter + 1][jter + 1] + graph[iter + 2][jter + 1]
            if ans < temp:
                ans = temp
        # case 17
        if iter + 2 < N and 0 <= jter - 1:
            temp = graph[iter][jter] + graph[iter + 1][jter] + graph[iter + 1][jter - 1] + graph[iter + 2][jter - 1]
            if ans < temp:
                ans = temp
        # case 18
        if iter + 1 < N and jter + 2 < M:
            temp = graph[iter][jter] + graph[iter][jter + 1] + graph[iter + 1][jter + 1] + graph[iter + 1][jter + 2]
            if ans < temp:
                ans = temp
        # case 19
        if 0 <= iter - 1 and jter + 2 < M:
            temp = graph[iter][jter] + graph[iter][jter + 1] + graph[iter - 1][jter + 1] + graph[iter - 1][jter + 2]
            if ans < temp:
                ans = temp
print(ans)
sys.exit(0)