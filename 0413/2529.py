k = int(input())
pt = list(input().split())
check = [False] * 10
ans = []
def inspect(a, parenthesis, b):
    a = int(a)
    b = int(b)
    if parenthesis == ">":
        return a > b
    else:
        return a < b
def go(num, index):
    if index == k + 1:
        ans.append(num)
        return
    for iter in range(10):
        if check[iter]:
            continue
        else:
            if index == 0:
                num = str(iter)
                check[iter] = True
                go(num, index + 1)
                check[iter] = False
            else:
                if inspect(num[index - 1], pt[index - 1], iter):
                    check[iter] = True
                    go(num + str(iter) , index + 1)
                    check[iter] = False
go("", 0)
ans.sort()
print(ans[-1])
print(ans[0])

        