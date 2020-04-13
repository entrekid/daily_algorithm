import sys
input = sys.stdin.readline
def go(sum , goal):
    global cnt
    if sum > goal:
        return 0
    elif sum == goal:
        return 1
    else:
        cnt = 0
        for iter in range(1, 4):
            cnt += go(sum + iter, goal)
    return cnt
test_case = int(input())
for _ in range(test_case):
    print(go(0, int(input())))