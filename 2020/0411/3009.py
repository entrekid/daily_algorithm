from collections import Counter
x = [0] * 3
y = [0] * 3
for iter in range(3):
    x[iter], y[iter] = map(int, input().rstrip().split())
axis_x = Counter(x)
axis_y = Counter(y)
for elem in axis_x:
    if axis_x[elem] == 1:
        result_x = elem
for elem in axis_y:
    if axis_y[elem] == 1:
        result_y = elem
print(result_x, result_y)
