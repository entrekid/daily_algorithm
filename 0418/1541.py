import sys
input = sys.stdin.readline
equation = input().rstrip()
ans = 0
minus = False
print(equation)
num = []
for elem in equation:
    if elem == "+" and not minus:
        ans += int("".join(num))
        num = []
    elif elem == "+" and minus:
        ans -= int("".join(num))
        num = []
    elif elem == "-":
        minus = True
        ans += int("".join(num))
        num = []
    else:
        num.append(elem)
print(ans) 

