import sys
input = sys.stdin.readline
num = int(input())
ans = 0
for _ in range(num):
    ans += int(input())
if ans > num / 2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")