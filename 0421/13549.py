from collections import deque
queue_0 = deque()
queue_1 = deque()
MAX = 200002
N, K = map(int, input().split())
check = [False] * MAX
dist = [0] * MAX
dist[N] = 0
check[N] = True
queue_0.append(N)
def inRange(x):
    if 0 <= x < MAX:
        return True
    return False
while queue_0:
    base = queue_0.popleft()
    # case 0 : 2 * x
    if inRange(2 * base) and not check[2 * base]:
        check[2 * base] = True
        dist[2 * base] = dist[base]
        queue_0.append(2 * base)
    # case 1 : x - 1
    if inRange(base - 1) and not check[base - 1]:
        check[base - 1] = True
        dist[base - 1] = dist[base] + 1
        queue_1.append(base - 1)
    # case 2 : x + 1
    if inRange(base + 1) and not check[base + 1]:
        check[base + 1] = True
        dist[base + 1] = dist[base] + 1
        queue_1.append(base + 1)
    if not queue_0:
        queue_0 = queue_1
        queue_1 = deque()
print(dist[K])