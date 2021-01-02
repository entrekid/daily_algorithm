num = input()
length = len(num)
ans = 0
base = 1
while base < length:
    start = '1' + '0' * (base - 1)
    end = '9' * base
    ans = ans + (int(end) - int(start) + 1) * base
    base += 1
start = '1' + '0' * (length - 1)
ans = ans + (int(num) - int(start) + 1) * length
print(ans)