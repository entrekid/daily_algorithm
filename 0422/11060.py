N = int(input())
num_list = list(map(int, input().split()))
D = [-1] * N
D[0] = 0
for iter in range(1, N):
    for jter in range(iter):
        if D[jter] != -1 and iter - jter <= num_list[jter]:
            if D[iter] == -1 or D[iter] > D[jter] + 1:
                D[iter] = D[jter] + 1
print(D[N - 1])
