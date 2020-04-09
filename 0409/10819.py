import sys
input = sys.stdin.readline

def next_permutations(num_list, size):
    iter = size - 1
    while iter > 0 and num_list[iter] <= num_list[iter - 1]:
        iter -= 1
    if iter <= 0:
        return False
    jter = size - 1
    while num_list[jter] <= num_list[iter - 1]:
        jter -= 1
    num_list[iter - 1], num_list[jter] = num_list[jter], num_list[iter - 1]
    kter = size - 1
    while iter < kter:
        num_list[iter], num_list[kter] = num_list[kter], num_list[iter]
        iter += 1
        kter -= 1
    return True
size = int(input())
num_list = list(map(int, input().rstrip().split()))
num_list.sort()
ans = 0
temp = 0
for iter in range(1, size):
    temp += abs(num_list[iter] - num_list[iter - 1])
if temp > ans:
    ans = temp
while next_permutations(num_list, size):
    temp = 0
    for iter in range(1, size):
        temp += abs(num_list[iter] - num_list[iter - 1])
    if temp > ans:
        ans = temp
print(ans)