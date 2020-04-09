import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num_list = list(map(int, input().rstrip().split()))
num_list.sort()
check = [False] * (N)
result = []
ans = []
def go(N, M, depth, base):
    if depth == M:
        ans.append(result.copy())
    else:
        compare = -1
        for iter in range(base, N):
            if check[iter]:
                continue
            elif not check[iter] and check[iter] != compare:
                check[iter] = True
                result.append(num_list[iter])
                go(N, M, depth + 1, iter)
                result.pop()
                check[iter] = False
                compare = num_list[iter]
go(N, M, 0, 0)
length = len(ans)
ans.sort()
for iter in range(length):
    if iter == 0:
        print(*ans[0])
    else:
        if ans[iter - 1] != ans[iter]:
            print(*ans[iter])