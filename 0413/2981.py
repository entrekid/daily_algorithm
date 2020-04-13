import sys
input = sys.stdin.readline
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
base = int(input())
num = []
for _ in range(N - 1):
    temp = int(input())
    num.append(abs(base - temp))
    base = temp
num_gcd = num[0]
for elem in num:
    num_gcd = gcd(elem, num_gcd)
ans = []
for iter in range(2, num_gcd + 1):
    if num_gcd % iter == 0:
        ans.append(iter)
print(*ans)