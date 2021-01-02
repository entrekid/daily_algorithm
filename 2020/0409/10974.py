def next_permutations(num_list):
    iter = len(num_list) - 1
    while iter > 0 and num_list[iter - 1] >= num_list[iter]:
        iter -= 1
    if iter <= 0:
        return False
    jter = len(num_list) - 1
    while num_list[jter] <= num_list[iter - 1]:
        jter -= 1
    num_list[iter - 1], num_list[jter] = num_list[jter], num_list[iter - 1]
    kter = len(num_list) - 1
    while iter < kter:
        num_list[iter], num_list[kter] = num_list[kter], num_list[iter]
        iter += 1
        kter -= 1
    return True
N = int(input())
num_list = list(range(1, N + 1))
print(*num_list)
while next_permutations(num_list):
    print(*num_list)