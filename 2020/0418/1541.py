import sys
input = sys.stdin.readline
equation = input().rstrip()
ans = 0
minus = False
num = []
for elem in equation:
    if elem == "+" and not minus:
        ans += int("".join(num))
        num = []
    elif elem == "+" and minus:
        ans -= int("".join(num))
        num = []
    elif elem == "-" and minus:
        ans -= int("".join(num))
        num = []
    elif elem == "-" and not minus:
        ans += int("".join(num))
        minus = True
        num = []
    else:
        num.append(elem)
if minus:
    ans -= int("".join(num))
else:
    ans += int("".join(num))
print(ans) 

