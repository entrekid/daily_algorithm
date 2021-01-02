from collections import Counter
N = int(input())
num_list = list(map(int, input().split()))
v = int(input())
print(Counter(num_list)[v])