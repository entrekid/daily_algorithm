N, M = map(int, input().split())
num_list = list(map(int, input().rstrip().split()))
num_list.sort()
check = [False] * N
result = []
ans = []
def go(N, M, index):
    if index == M:
        ans.append(result.copy())
        return
    else:
        for iter in range(N):
            if check[iter]:
                continue
            else:
                check[iter] = True
                result.append(num_list[iter])
                go(N, M, index + 1)
                check[iter] = False
                result.pop()
go(N, M, 0)
length = len(ans)
ans.sort()
for iter in range(length):
    if iter == 0:
        print(*ans[iter], sep = " ", end = "\n")
    elif iter - 1 >= 0:
        if ans[iter] != ans[iter - 1]:
            print(*ans[iter], sep = " ", end = "\n")