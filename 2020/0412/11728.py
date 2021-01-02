import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))
C = A + B
C.sort()
print(*C)