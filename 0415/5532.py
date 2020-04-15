L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
if A % C == 0:
    kor = A // C
else:
    kor = A // C + 1

if B % D == 0:
    math = B // D
else:
    math = B // D + 1

rest = max(math, kor)
print(L - rest)