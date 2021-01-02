num = int(input())
def length(base, num):
    ans = ""
    ans += " " * (base - num)
    for iter in range(2 * num - 1):
        if iter % 2 == 0:
            ans += "*"
        else:
            ans += " "
    return ans
for iter in range(1, num + 1):
    print(length(num, iter))