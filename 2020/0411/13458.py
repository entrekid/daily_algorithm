import sys
N = int(input())

ans = []
A = list(map(int, input().rstrip().split()))
B, C = map(int, input().rstrip().split())
for iter in range(N):
    if A[iter] >= B:
        if (A[iter] - B) % C:
            temp = (A[iter] - B) // C + 1
            temp += 1 # 주감독관 수 까지
            ans.append(temp)
        else:
            temp = (A[iter] - B) // C + 1
            ans.append(temp)
    else:
        ans.append(1)
print(sum(ans))