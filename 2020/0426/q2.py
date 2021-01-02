import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ability = {}
for iter in range(1, N + 1):
    x, y = map(int, input().split())
    ability[iter] = (x, y)
graph = [[] for _ in range(N + 1)]
for _ in range(1, M + 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 팀 정하기
team = [0] * (N + 1)
team_no = 1
def dfs(order):
    global team_no
    team[order] = team_no
    for elem in graph[order]:
        if team[elem] == 0:
            team[elem] = team_no
            dfs(elem)
for iter in range(1, N + 1):
    if team[iter] == 0:
        dfs(iter)
        team_no += 1
# 혹시 나중 여기 인덱스 체크
stat = [[-1, -1, -1, -1]] * team_no
for elem in range(1, N + 1):
    x, y = ability[elem]
    x_min, x_max, y_min, y_max = stat[team[elem]]
    if x_min == -1 or x_min > x:
        x_min = x
    if x_max < x:
        x_max = x
    if y_min == -1 or y_min > y:
        y_min = y
    if y_max < y:
        y_max = y
    stat[team[elem]] = [x_min, x_max, y_min, y_max]
ans = -1
for elem in range(1, team_no):
    x_min, x_max, y_min, y_max = stat[elem]
    temp = 2 * (x_max - x_min + y_max - y_min)
    if ans < temp:
        ans = temp
print(ans)

