from itertools import combinations
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
ans = []
for comb in combinations(num_list, 3):
    comb_list = list(comb)
    num_sum = sum(comb_list)
    if num_sum > M:
        continue
    comb_list.append(num_sum)
    ans.append(comb_list)
ans.sort(key = lambda x : x[-1])
print(ans[-1][-1])