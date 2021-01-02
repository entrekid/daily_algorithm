import sys
input = sys.stdin.readline
num_list = []
for _ in range(9):
    num_list.append(int(input()))
num_list.sort()
total = sum(num_list)
go = True
x = total - 100
for iter in range(9):
    for jter in range(iter + 1, 9):
        if (num_list[iter] + num_list[jter]) == x:
            base1 = iter
            base2 = jter
            go = False
            break
    if not go:
        break
for kter in range(9):
    if kter == base1 or kter == base2:
        continue
    print(num_list[kter])
            