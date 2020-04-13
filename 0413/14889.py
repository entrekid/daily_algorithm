import sys
input = sys.stdin.readline
N = int(input())
S = [list(map(int, input().rstrip().split())) for _ in range(N)]
MAX = 100000
def go(index, first, second):
    # 성공하는 경우
    if index == N:
        team_first = 0
        team_second = 0
        for elem1 in first:
            for elem2 in first:
                if elem1 == elem2:
                    continue
                else: 
                    team_first += S[elem1][elem2]
        for elem1 in second:
            for elem2 in second:
                if elem1 == elem2:
                    continue
                else: 
                    team_second += S[elem1][elem2]
        diff = abs(team_first - team_second)
        return diff    
    # 실패하는 경우
    if len(first) > N // 2:
        return MAX
    if len(second) > N // 2:
        return MAX
    # 다음 경우
    else:
        first.append(index)
        ret1 = go(index + 1, first, second)
        first.pop()
        second.append(index)
        ret2 = go(index + 1, first, second)
        second.pop()
        return ret1 if ret1 < ret2 else ret2
print(go(0, [], []))
