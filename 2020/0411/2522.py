num = int(input())
for iter in range(1, num + 1):
    print(" " * (num - iter) + "*" * iter)
for jter in range(num - 1, 0, -1):
    print(" " * (num - jter) + "*" * jter)