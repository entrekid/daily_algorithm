num = int(input())
for iter in range(1, num + 1):
    print(" " * (num - iter) +  "*" * (2 * iter - 1))
for jter in range(num - 1, 0, -1):
    print(" " * (num - jter) +  "*" * (2 * jter - 1))