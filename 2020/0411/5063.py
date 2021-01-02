import sys
test_case = int(input())
for _ in range(test_case):
    r, e, c = map(int, input().rstrip().split())
    base = r 
    compare = (e - c)
    if base < compare:
        print("advertise")
    elif base == compare:
        print("does not matter")
    else:
        print("do not advertise")