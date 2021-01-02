import math
M = int(input())
N = int(input())
num_list = []
total = 0
cnt = 0
ans = 10001
for iter in range(M, N + 1):
    if iter % (math.sqrt(iter)) == 0:
        if iter < ans:
            ans = iter
        cnt += 1
        total += iter
if cnt:
    print(total)
    print(ans)
else:
    print(-1)