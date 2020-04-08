import sys
input = sys.stdin.readline

def check(num):
    if num == 0:
        return False if broken[num] else True
    while num:
        if broken[num % 10]:
            return False
        num //= 10
    return True
target = int(input())
length = len(str(target))
broken_no = int(input())
if broken_no:
    broken_buttons = list(map(int, input().rstrip().split()))
    if target == 100:
        print(0)
        sys.exit(0)
else:
    if target == 100:
        print(0)
        sys.exit(0)
    print(length if length < abs(target - 100) else abs(target - 100))
    sys.exit(0)
broken = [False] * 10
for broken_button in broken_buttons:
    broken[broken_button] = True
if check(target):
    """
    1. 100번인 경우에
    2. 길이를 누르는 것보다 +, - 횟수가 작은 것
    3. 길이를 누르는 것이 더 짧을 때
    """
    print(abs(target - 100) if abs(target - 100) < length else length)
else:
    ans = 1000000
    for num in range(1000000):
        begin = num
        length = len(str(begin))
        if not check(num):
            continue
        else:
            temp = length + abs(target - begin)
            if temp < ans:
                ans = temp
    print(ans if ans < abs(target - 100) else abs(target - 100))
    sys.exit(0)



        