N, K = map(int, input().split())
num_list = list(map(int, input().split()))
x = num_list.index(min(num_list))
left = x
right = N - x - 1
rem = left % (K - 1)
cnt = 0
if rem:
    cnt = 1
    left -= rem
    right = right - (K - 1 - rem)
cnt = cnt + (left // (K - 1))
if (right % (K - 1)) == 0:
    cnt = cnt + ((right) // (K - 1))
elif (right % (K - 1) != 0):
    cnt = cnt + ((right) // (K - 1))
    cnt += 1
print(cnt)