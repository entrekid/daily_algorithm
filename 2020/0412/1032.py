import sys
input = sys.stdin.readline
N = int(input())
all = [input().rstrip() for _ in range(N)]
ans = all[0]
length = len(ans)
ret = ""
for index in range(length):
    base = ans[index]
    for jter in range(1, N):
        if all[jter][index] == base:
            continue
        else:
            ret += "?"
            break
    else:
        ret += base
print(ret)
