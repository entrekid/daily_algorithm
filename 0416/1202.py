import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
item = []
C = [0] * K
for _ in range(N):
    item.append(list(map(int, input().rstrip().split())))
for iter in range(K):
    C[iter] = [int(input()), False]
item.sort(key = lambda x : x[1], reverse = True)
C.sort()
ans = 0
for weight, value in item:
    for iter in range(K):
        if C[iter][0] >= weight:
            if C[iter][1]:
                continue
            else:
                C[iter][1] = True
                # 보석을 가방에 넣는다. (보석과 가방의 쌍 모두 제거)
                ans += value
                break
        else:
            continue
print(ans)
