import sys
N = int(input())
start = 0
end = N - 1
if start == end:
    print(" " * (N - 1) + "*")
    sys.exit(0)
else:
    # start
    print(" " * (N - 1) + "*")
    # middle
    for iter in range(1, N - 1):
        print(" " * (N - iter - 1) + "*" + " " * (2 * iter - 1) + "*")
    # end
    print("*" * (2 * N - 1))
