import sys
input = sys.stdin.readline
N = int(input())
T = []
P = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
D = [0] * (N)
for iter in range(0, N):
    # 상담을 한다
    if iter + T[iter] < N:
        D[iter + T[iter]] = max(D[iter] + P[iter], D[iter + T[iter]])
    # 하지 않는다
    if iter + 1 < N:
        D[iter + 1] = max(D[iter + 1], D[iter])
print(D)