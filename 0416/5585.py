N = int(input())
N = 1000 - N
money = [500, 100, 50, 10, 5, 1]
cnt = 0
while N:
    for elem in money:
        if N >= elem:
            N -= elem
            cnt += 1
            break
print(cnt)
