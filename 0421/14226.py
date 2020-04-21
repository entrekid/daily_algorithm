from collections import deque
"""
1. (s, c) -> (s, s)
2. (s, c) -> (s + c, c)
3. (s, c) -> (s - 1, c)
"""
N = int(input())
check = [[False] * (N + 1) for _ in range(N + 1)]
dist = [[0] * (N + 1) for _ in range(N + 1)]
queue = deque()
base = (1, 0)
queue.append(base)
check[1][0] = True
def inRange(x, y):
    if 0 <= x <= N and 0 <= y <= N:
        return True
    return False
while queue:
    base = queue.popleft()
    s, c = base
    # case 1
    if not check[s][s]:
        check[s][s] = True
        queue.append((s, s))
        dist[s][s] = dist[s][c] + 1
    # case 2
    if inRange(s + c, c) and not check[s + c][c]:
        check[s + c][c] = True
        queue.append((s + c, c))
        dist[s + c][c] = dist[s][c] + 1
    # case 3
    if inRange(s - 1, c) and not check[s - 1][c]:
        check[s - 1][c] = True
        queue.append((s - 1, c))
        dist[s - 1][c] = dist[s][c] + 1

print(sorted(dist[N])[1])