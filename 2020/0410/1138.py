from itertools import permutations
import sys
num = int(input())
num_list = list(map(int, input().split()))
def check(num_list, num):
    ans = [0] * num
    for iter in range(num):
        for jter in range(0, iter):
            if num_list[iter] < num_list[jter]:
                ans[num_list[iter] - 1] += 1
    return ans




for perm in permutations(num_list):
    next = False
    check_list = check(perm, num)
    print(check_list)
    for iter in range(num):
        if check_list[iter] != perm[iter]:
            next = True
            break
        else:
            continue
    if next:
        continue
    else:
        print(check_list)
        break
