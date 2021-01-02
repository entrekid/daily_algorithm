N = int(input())
N -= 1
ans = 0
div = 0
while True:
    if N == 0:
        print(1)
        break
    else:
        ans += 1
        div = div + ans
        if N <= 6 * div:
            print(ans + 1)
            break
 