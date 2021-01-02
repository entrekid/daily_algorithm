num = int(input())
for iter in range(num, 0, -1):
    print(" " * (num - iter) + (2 * iter - 1) * "*")
for jter in range(2, num + 1):
    print(" " * (num - jter) + (2 * jter - 1) * "*")