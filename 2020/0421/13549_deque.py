from collections import deque
queue = deque()
MAX = 200002
N, K = map(int, input().split())
check = [False] * MAX
dist = [0] * MAX
def inRange(x):
    return 0 <= x < MAX
check[N] = True
queue.append(N)
while queue:
    base = queue.popleft()
    if inRange(base * 2) and not check[base * 2]:
        check[base * 2] = True
        dist[base * 2] = dist[base]
        queue.appendleft(base * 2)
    if inRange(base + 1) and not check[base + 1]:
        check[base + 1] = True
        dist[base + 1] = dist[base] + 1
        queue.append(base + 1)
    if inRange(base - 1) and not check[base - 1]:
        check[base - 1] = True
        dist[base - 1] = dist[base] + 1
        queue.append(base - 1)
print(dist[K])