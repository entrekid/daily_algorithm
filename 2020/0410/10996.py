num = int(input())
first_line = ""
second_line = ""
for iter in range(num):
    if iter % 2 == 0:
        first_line += "*"
    else:
        first_line += " "
for iter in range(num):
    if iter % 2 == 1:
        second_line += "*"
    else:
        second_line += " "
if num == 1:
    print(first_line)
else:
    while num > 0:
        print(first_line)
        print(second_line)
        num -= 1