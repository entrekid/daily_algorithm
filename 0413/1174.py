import sys
sys.setrecursionlimit(10 ** 6)
ans = []
num = []
def dfs(depth, start, base):
    """
    start : 시작하는 수
    base : 이번 depth 시작 수
    """
    if depth == start:
        ans.append("".join(num))
        return
    elif base == 0:
        ans.append("".join(num))
        return
    else:
        for iter in range(base):
            num.append(str(iter))
            dfs(depth + 1, start, iter)
            num.pop()

for iter in range(11):
    for jter in range(11):
        dfs(0, iter, jter)
ans = list(set(ans))
ans = ans[1:]
ans = list(map(int, ans))
ans.sort()
N = int(input())
N -= 1
if N <= 1022:
    print(ans[N])
else:
    print(-1)