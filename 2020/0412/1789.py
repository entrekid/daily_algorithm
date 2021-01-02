S = int(input())
i = 1
while True:
    if S < i * (i + 1) / 2 :
        print(i - 1)
        break
    i += 1
    