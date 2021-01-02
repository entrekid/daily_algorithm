num = list(input())
num.sort(reverse = True)
num = int("".join(num))
print(num if num % 30 == 0 else -1)
