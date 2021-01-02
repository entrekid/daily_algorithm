import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num_list = list(map(int, input().rstrip().split()))
num_list.sort()
check = [False] * N
result = []
def go(N, M, index, base_idx):
    if index == M:
        print(*result, sep = " ", end = "\n")
    else:
        for iter in range(base_idx, N):
            if check[iter]:
                continue
            check[iter] = True
            result.append(num_list[iter])
            go(N, M, index + 1, iter)
            check[iter] = False
            result.pop()
go(N, M, 0, 0)
