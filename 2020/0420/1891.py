import sys
input = sys.stdin.readline
d, num = input().split()
x, y = map(int, input().split())
size = 2 ** int(d)
graph = [[0] * size for _ in range(size)]
print(graph)