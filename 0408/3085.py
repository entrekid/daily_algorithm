import sys
input = sys.stdin.readline
size = int(input())
graph = [list(input().rstrip()) for _ in range(size)]
def check(graph, size):
    ret = 1
    for iter in range(size):
        cnt = 1
        for jter in range(size - 1):
            if graph[iter][jter] == graph[iter][jter + 1]:
                cnt += 1
            else:
                cnt = 1
            
            if ret < cnt:
                ret = cnt
        cnt = 1
        for jter in range(size - 1):
            if graph[jter][iter] == graph[jter + 1][iter]:
                cnt += 1
            else:
                cnt = 1
            if ret < cnt:
                ret = cnt
    return ret

ans = 0
for iter in range(size):
    for jter in range(size - 1):
        # 행에 대한 검토
        graph[iter][jter], graph[iter][jter + 1] = graph[iter][jter + 1], graph[iter][jter]
        temp = check(graph, size)
        if ans < temp:
            ans = temp
        graph[iter][jter], graph[iter][jter + 1] = graph[iter][jter + 1], graph[iter][jter]

        graph[jter][iter], graph[jter + 1][iter] = graph[jter + 1][iter], graph[jter][iter]
        temp = check(graph, size)
        if ans < temp:
            ans = temp
        graph[jter][iter], graph[jter + 1][iter] = graph[jter + 1][iter], graph[jter][iter]
print(ans)