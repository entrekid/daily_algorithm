import sys
input = sys.stdin.readline

def next_permutation(num_list):
    i = len(num_list) - 1
    while i > 0 and num_list[i - 1] >= num_list[i]:
        i -= 1
    if i <= 0:
        return False
    jter = len(num_list) - 1
    while num_list[jter] <= num_list[i - 1]:
        jter -= 1
    num_list[jter], num_list[i - 1] =  num_list[i - 1], num_list[jter]
    kter = len(num_list) - 1
    while i < kter:
        num_list[i], num_list[kter] = num_list[kter], num_list[i]
        i += 1
        kter -= 1
    return True
num = int(input())
num_list = list(map(int, input().rstrip().split()))
if next_permutation(num_list):
    print(*num_list)
else:
    print(-1)
