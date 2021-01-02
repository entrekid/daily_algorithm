import sys
input = sys.stdin.readline

result = []
def dfs(index, num_list, start, size):
    if index == 6:
        print(*result)
        return
    else:
        for iter in range(start, size):
            if check[iter]:
                continue
            else:
                check[iter] = True
                result.append(num_list[iter])
                dfs(index + 1, num_list, iter, size)
                result.pop()
                check[iter] = False
    return

while True:
    size, *num_list = map(int, input().rstrip().split())
    if size == 0:
        break
    else:
        num_list.sort()
        check = [False] * size
        dfs(0, num_list, 0, size)
        print()