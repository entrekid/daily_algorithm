a = [0, 0, 0, 0]
ans = 0
for iter in range(4):
    out, inward = map(int, input().split())
    if iter:
        a[iter] = a[iter - 1] - out + inward
        if a[iter] > ans:
            ans = a[iter]
    else:
        a[iter] = inward
        if ans > a[iter]:
            ans = a[iter]
print(ans)
