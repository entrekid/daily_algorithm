import sys
input = sys.stdin.readline
N = int(input())
S = [list(map(int, input().rstrip().split())) for _ in range(N)]

ans = -1
for iter in range(1 << N):
    team1 = []
    team2 = []
    len1 = 0
    len2 = 0
    for jter in range(N):
        if iter & (1 << jter):
            team1.append(jter)
            len1 += 1
        else:
            team2.append(jter)
            len2 += 1
    if len1 != N//2:
        continue
    else:
        tot1 = 0
        tot2 = 0
        for iter in range(N//2):
            for jter in range(N // 2):
                if iter == jter:
                    continue
                else:
                    tot1 += S[team1[iter]][team1[jter]]
                    tot2 += S[team2[iter]][team2[jter]]
        diff = abs(tot1 - tot2)
        if ans > diff or ans == -1:
            ans = diff
print(ans)