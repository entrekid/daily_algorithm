import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    N = int(input())
    num_list = list(map(int, input().rstrip().split()))
    print(sum(num_list))