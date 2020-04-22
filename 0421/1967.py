import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
