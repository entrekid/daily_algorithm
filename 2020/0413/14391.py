import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(N)]
ans = 0
"""
가로를 0
세로를 1로 설정
"""
for s in range(1 << N*M):
    total = 0
    for row in range(N):
        temp = 0
        for col in range(M):
            kth = row * M + col
            if (s & (1 << kth)) == 0:
                temp = temp * 10 + graph[row][col]
            else:
                total += temp
                temp = 0
        total += temp
    
    for col in range(M):
        temp = 0
        for row in range(N):
            kth = row * M + col
            if (s & (1 << kth)) != 0:
                temp = temp * 10 + graph[row][col]
            else:
                total += temp
                temp = 0
        total += temp
    if ans < total:
        ans = total
print(ans)
