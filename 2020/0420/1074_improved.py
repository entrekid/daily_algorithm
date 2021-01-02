N, r, c = map(int, input().split())
width = 2 ** N
cnt = 0
def check(x, y, width):
    base = width // 2
    if x < base and y < base:
        return 1
    elif x < base and y >= base:
        return 2
    elif x >= base and y < base:
        return 3
    else:
        return 4
def solve(x, y, width):
    global cnt
    quartile = check(x, y, width)
    if width == 0:
        print(cnt)
        return
    width = width // 2
    if quartile == 1:
        solve(x, y, width)
    elif quartile == 2:
        cnt += (width) ** 2
        solve(x, y - width, width)
    elif quartile == 3:
        cnt += (width) ** 2 * 2
        solve(x - width, y, width)
    elif quartile == 4:
        cnt += (width) ** 2 * 3
        solve(x - width, y - width, width)
solve(r, c, width)