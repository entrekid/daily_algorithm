import sys
N = int(input())
t_list = []
p_list = []
for _ in range(N):
    a, b = map(int, input().split())
    t_list.append(a)
    p_list.append(b)

def go(day, total):
    if day == N:
        return total
    elif day > N:
        return 0
    else:
        ret1 = go(day + t_list[day], total + p_list[day])
        ret2 = go(day + 1, total)
        return ret1 if ret1 > ret2 else ret2
print(go(0, 0))