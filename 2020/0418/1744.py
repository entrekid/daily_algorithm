import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
num = []
def calc(num_list, length, ans):
    if length == 0:
        return ans
    if length == 1:
        ans += num_list[0]
        return ans
    else:
        while length:
            if length == 0:
                return ans
            if length == 1:
                ans += num_list[0]
                return ans
            a = num_list.popleft()
            b = num_list.popleft()
            if a != 1 and b != 1:
                ans += a*b
            else:
                ans = ans + a + b
            length -= 2
        return ans
    

for _ in range(N):
    num.append(int(input()))
plus = [elem for elem in num if elem > 0]
minus = [elem for elem in num if elem <= 0]
ans = 0
plus.sort(reverse = True)
minus.sort()
plus = deque(plus)
minus = deque(minus)
n_plus = len(plus)
n_minus = len(minus)
ans = calc(plus, n_plus, ans) + calc(minus, n_minus, ans)
print(ans)

