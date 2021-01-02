import sys
input = sys.stdin.readline
N = int(input())
line = []
for _ in range(N):
    start, end = map(int, input().split())
    if start <= end:
        line.append((start, end))
    else:
        line.append((end, start))
line.sort(key = lambda x : (x[0], x[1]))
total = line[0][1] - line[0][0]
start_b = line[0][0]
end_b = line[0][1]
for elem in line:
    start, end = elem
    if start_b <= start and end <= end_b:
        continue
    elif start_b <= start <= end_b and end_b < end:
        total += (end - end_b)
        end_b = end
    else:
        start_b = start
        end_b = end
        total += (end - start)
print(total)
