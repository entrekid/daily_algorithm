import sys
input = sys.stdin.readline
x = 1
y = 1
cnt = 1
total = 2
N = int(input())
while True:
    if x == total or y == total:
        total += 1
        if x == total - 1:
            y = 1
        else:
            x = 1
    if N == cnt:
        print(str(x) + "/" + str(y))
        break
    if total % 2:
        # total이 홀수
        x += 1
        y -= 1
        cnt += 1
    else:
        x -= 1
        y += 1
        cnt += 1