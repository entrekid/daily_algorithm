from collections import deque
N, K = map(int, input().split())
check = [False] * 100001
dist = [-1] * 100001
parent = [-1] * 100001
queue = deque()
queue.append(N)
check[N] = True
dist[N] = 0
def inRange(num):
    if 0 <= num <= 100000:
        return True
    else:
        return False
while queue:
    base = queue.popleft()
    if inRange(base + 1) and not check[base + 1]:
        check[base + 1] = True
        dist[base + 1] = dist[base] + 1
        parent[base + 1] = base
        queue.append(base + 1)
    if inRange(base - 1) and not check[base - 1]:
        check[base - 1] = True
        dist[base - 1] = dist[base] + 1
        parent[base - 1] = base
        queue.append(base - 1)
    if inRange(2 * base) and not check[2 * base]:
        check[2 * base] = True
        dist[2 * base] = dist[base] + 1
        parent[2 * base] = base
        queue.append(2 * base)
print(dist[K])
ans = []
base = K
while parent[base] != -1:
    ans.append(str(base))
    base = parent[base]
ans.append(str(N))
while ans:
    print(ans.pop(), end = " ")
print()