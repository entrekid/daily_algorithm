n = int(input())
# increase
for iter in range(1, n):
    print("*" * iter + " " * 2 * (n - iter)  +"*" * iter)
# middle
print("*" * 2 * n)
# end
for iter in range(n - 1 , 0, -1):
    print("*" * iter + " " * 2 * (n - iter)  +"*" * iter)