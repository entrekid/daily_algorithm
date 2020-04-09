import sys
input = sys.stdin.readline

def number(sum_till_now, target):
    if sum_till_now > target:
        return 0
    if sum_till_now == target:
        return 1
    now = 0
    for iter in range(1, 4):
        now += number(sum_till_now + iter, target)
    return now
test_case = int(input())
for _ in range(test_case):
    n = int(input())
    print(number(0, n))