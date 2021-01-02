num_list = list(map(int, input().split()))
answer_list = []
def check(num_list):
    if len(num_list) == 1 and num_list[0] == 1:
        return True
    else:
        return False
def translate(num_list):
    length = len(num_list)
    if length == 1:
        return [1]
    base = 1
    result = []
    for iter in range(length - 1):
        if num_list[iter] == num_list[iter + 1]:
            base += 1
        else:
            result.append(base)
            base = 1
    result.append(base)
    return result.copy()
ans = 0
while not check(num_list):
    ans += 1
    print(num_list)
    num_list = translate(num_list)
print(ans)
