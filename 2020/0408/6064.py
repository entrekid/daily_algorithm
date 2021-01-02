import sys
input = sys.stdin.readline
test_case = int(input())
for _ in range(test_case):
    M, N, x, y = map(int, input().rstrip().split())
    x -= 1
    y -= 1
    year = x
    a = x % M
    b = x % N
    while b != y and year <= M * N:
        a = (a + M) % M
        b = (b + M) % N
        year += M
    if a == x and y == b:
        print(year + 1)
    else:
        print(-1)
        