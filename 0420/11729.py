N = int(input())
cnt = 0
ans = []
def solve(n, x, y):
    global cnt
    if n == 0:
        return
    solve(n - 1, x, 6 - x - y)
    ans.append((x, y))
    cnt += 1
    solve(n - 1, 6- x- y, y)
solve(N, 1, 3)
print(cnt)
for elem in ans:
    print(*elem)