E, S, M = map(int, input().split())
year = 0
e, s, m = 0, 0, 0
while True:
    e += 1
    s += 1
    m += 1
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1
    year += 1
    if e == E and s == S and m == M:
        break
print(year)