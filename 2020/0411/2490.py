import sys
input = sys.stdin.readline
from collections import Counter
def check(num_list):
    base = Counter(num_list)[0]
    if base == 1:
        print("A")
    elif base == 2:
        print("B")
    elif base == 3:
        print("C")
    elif base == 4:
        print("D")
    else:
        print("E")
    return

for iter in range(3):
    check(list(map(int, input().rstrip().split())))