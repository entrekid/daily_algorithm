import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip()))
B = list(map(int, input().rstrip()))
check1 = [int(A[iter] == B[iter]) for iter in range(N)]
check2 = [int(A[iter] == B[iter]) for iter in range(N)]
def flip(index, check):
    if index == N - 1:
        check[index] = 1 - check[index]
        check[index - 1] = 1 - check[index - 1]
    else:
        for iter in range(-1, 2):
            check[index + iter] = 1 - check[index + iter]
cnt1, cnt2 = 0, 0
MAX = 100001
# 0번 스위치를 눌렀을 때
check1[0] = 1 - check1[0]
check1[1] = 1 - check1[1]
cnt1 += 1
for iter in range(1, N):
    if not check1[iter - 1]:
        cnt1 += 1
        flip(iter, check1)
    else:
        continue
if not check1[N - 1]:
    cnt1 = MAX

# 0번 스위치를 누르지 않았을 때
for iter in range(1, N):
    if not check2[iter - 1]:
        cnt2 += 1
        flip(iter, check2)
    else:
        continue
if not check2[N - 1]:
    cnt2 = MAX

ans = min(cnt1, cnt2)
if ans == MAX:
    print(-1)
else:
    print(ans)