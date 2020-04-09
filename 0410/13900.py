num = int(input())
num_list = list(map(int, input().split()))
ret1 = sum(num_list) ** 2
ret2 = 0
for elem in num_list:
    ret2 += elem ** 2
print(int((ret1 - ret2) * 0.5))
