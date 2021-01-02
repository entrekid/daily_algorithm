x, y = map(int, input().split())
day = {}
num_31 = [1, 3, 5, 7, 8, 10]
num_28 = [2]
num_30 = [4, 6, 9, 11]
for month in num_31:
    day[month] = 31
for month in num_30:
    day[month] = 30
day[2] = 28
now = 0
for iter in range(1, x):
    now += day[iter]
now += y
result = now % 7
day_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
result_dict = {}
for iter in range(7):
    result_dict[iter] = day_list[iter]

print(result_dict[result])