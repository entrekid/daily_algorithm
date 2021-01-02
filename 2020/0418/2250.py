import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
tree = {}
info = {}
width = 1
height = 0
def inOrder(root, depth):
    global width
    global height
    if tree[root][0] != -1:
        inOrder(tree[root][0], depth + 1)
    info[root] = [depth, width]
    if depth > height:
        height = depth
    width += 1
    if tree[root][1] != -1:
        inOrder(tree[root][1], depth + 1)
parent = [-1] * (N + 1)
parent[0] = 0
for _ in range(N):
    root, left, right = map(int, input().rstrip().split())
    tree[root] = [left, right] # 저장된 값은 모두 string
    if left != -1:
        parent[left] = root
    if right != -1:
        parent[right] = root
root = parent.index(-1)
inOrder(root, 1)
ans = [(1, 0)] * (height + 1)
for jter in range(1, height + 1):
    num = []
    for iter in range(1, N + 1):
        if info[iter][0] == jter:
            num.append(info[iter][1])
    ans[jter] = (jter, max(num) - min(num) + 1)
ans.sort(key = lambda x : (x[1], -x[0]), reverse = True)
print(*ans[0])