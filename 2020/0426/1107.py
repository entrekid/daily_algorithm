target = int(input())
broken = int(input())
broken_list = list(map(int, input().split()))
"""
1. 시작점을 정한다.
2. 시작점 안에 망가진 것이 있나 확인
3. 있다면 패스 없다면 시작점 길이 + 채널과의 차이
4. 
"""
ans = 10000001
def check(num):
    num = str(num)
    for elem in num:
        if int(elem) in broken_list:
            return False
    return True

for base in range(1000001):
    if check(base):
        temp1 = len(str(base)) + abs(target - base)
        temp2 = abs(target - 100)
        if ans > temp1:
            ans = temp1
        if ans > temp2:
            ans = temp2
print(ans)