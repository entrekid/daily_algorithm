import sys
input = sys.stdin.readline

N = int(input())
T = [0] * N
P = [0] * N
for iter in range(N):
    T[iter], P[iter] = map(int, input().split())

ans = 0
def go(sum, day, deadline):
    global ans
    if day == deadline:
        if ans < sum:
            ans = sum
        return
    elif day > deadline:
        return
    else:
        go(sum + P[day], day + T[day], deadline)
        go(sum, day + 1, deadline)
go(0, 0, N)
print(ans)