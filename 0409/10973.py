import sys
input = sys.stdin.readline

def prev_permutation(num_list):
    i = len(num_list) - 1
    while i > 0 and num_list[i - 1] <= num_list[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(num_list) - 1
    while num_list[j] >= num_list[i - 1]:
        j -= 1
    num_list[i - 1], num_list[j] = num_list[j], num_list[i - 1]
    k = len(num_list) - 1
    while i < k:
        num_list[i], num_list[k] = num_list[k], num_list[i]
        i += 1
        k -= 1
    return True
    
num = int(input())
num_list = list(map(int, input().rstrip().split()))
if prev_permutation(num_list):
    print(*num_list)
else:
    print(-1)