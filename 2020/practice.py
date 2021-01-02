N, K = map(int, input().split())
num_list = list(map(int, input().split()))
num_idx = num_list.index(min(num_list))
MAX = 1000000
ans = MAX
for iter in range(K):
    cnt = 1
    left = num_idx - (K - 1 - iter)
    right = N - num_idx - 1 - iter
    while left > 0:
        left -= (K - 1)
        cnt += 1
    while right > 0:
        right -= (K - 1)
        cnt += 1
        print(cnt)
    if ans > cnt:
        ans = cnt
print(ans)