import sys
input = sys.stdin.readline

ans = []
for iter in range(1, 6):
    num_list = list(map(int, input().rstrip().split()))
    ans.append([iter, sum(num_list)])
ans.sort(key = lambda x : x[1], reverse = True)
print(*ans[0])
