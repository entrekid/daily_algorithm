import sys
input = sys.stdin.readline

M = int(input())
s = 0
for _ in range(M):
    order, *num = input().rstrip().split()
    if num:
        base = int(num[0]) - 1
        if order == "add":
            s = s | (1 << base)
        elif order == "remove":
            s = s & ~(1 << base)
        elif order == "check":
            print(1 if s & (1 << base) else 0)
        elif order == "toggle":
            s = s ^ (1 << base)
    elif order == "all":
        s = (1 << (20)) - 1
    elif order == "empty":
        s = 0
