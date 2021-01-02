import sys
input = sys.stdin.readline
from collections import deque

test_case = int(input())
def check(string):
    cursor1 = deque()
    cursor2 = deque()
    for word in string:
        if word == "<":
            if cursor1:
                cursor2.appendleft(cursor1.pop())
        elif word == ">":
            if cursor2:
                cursor1.append(cursor2.popleft())
        elif word == "-":
            if cursor1:
                cursor1.pop()
        else:
            cursor1.append(word)
    print("".join(cursor1) + "".join(cursor2))
for _ in range(test_case):
    check(input().rstrip())
    
