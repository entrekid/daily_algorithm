N, M, K = map(int, input().split())
ans = 0
if N == 2*M:
    ans = N
elif N > 2 * M:
    K -= (N - 2 * M)
    ans = M
else:
    K -= (2 * M - N)
    ans = N