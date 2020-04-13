N, K = map(int, input().split())
ans = []
cnt = 0
for iter in range(1, N + 1):
    if N % iter == 0:
        cnt += 1
        ans.append(iter)
if cnt < K:
    print(0)
else:
    print(ans[K - 1])