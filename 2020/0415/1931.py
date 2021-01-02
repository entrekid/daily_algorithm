import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append([start, end])
meetings.sort(key = lambda x : (x[1], x[0]))
cnt = 0
begin = 0
for iter in range(N):
    if begin <= meetings[iter][0]:
        begin = meetings[iter][1]
        cnt += 1
print(cnt)