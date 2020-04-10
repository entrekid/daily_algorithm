import sys
input = sys.stdin.readline

def check(a, b):
    if a % b == 0:
        print("multiple")
    elif b % a == 0:
        print("factor")
    else:
        print("neither")
while True:
    a, b = map(int, input().rstrip().split())
    if a == 0 and b == 0:
        sys.exit(0)
    else:
        check(a, b)
