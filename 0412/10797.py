from collections import Counter
num = int(input())
num_list = list(map(int, input().split()))
num_cnt = Counter(num_list)
print(num_cnt[num])