N = int(input())
iter = 1
cnt = 0
while N:
    cnt += 1
    N -= iter
    iter += 1
    if iter > N:
        iter = 1
print(cnt)
    