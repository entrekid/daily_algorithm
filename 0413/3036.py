N = int(input())
num_list = list(map(int, input().split()))
base = num_list[0]
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
gcd_list = list(gcd(elem, base) for elem in num_list)

for iter in range(1, N):
    print(str(base // gcd_list[iter]) + "/" + str(num_list[iter] // gcd_list[iter]))