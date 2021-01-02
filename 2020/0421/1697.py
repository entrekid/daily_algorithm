from collections import deque
check = [False] * 100001
dist = [-1] * 100001
N, K = map(int, input().split())
queue = deque()
queue.append(N)
check[N] = True
dist[N] = 0
def inRange(x):
    if 0 <= x <= 100000:
        return True
    else:
        return False
while queue:
    base = queue.popleft()
    check[base] = True
    if inRange(base + 1) and not check[base + 1]:
        check[base + 1] = True
        queue.append(base + 1)
        dist[base + 1] = dist[base] + 1
    if inRange(base - 1) and not check[base - 1]:
        check[base - 1] = True
        queue.append(base - 1)
        dist[base - 1] = dist[base] + 1
    if inRange(2* base) and not check[2 * base]:
        check[2 * base] = True
        queue.append(2 * base)
        dist[2 * base] = dist[base] + 1
print(dist[K])