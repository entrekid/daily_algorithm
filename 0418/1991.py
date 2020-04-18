import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
tree = {}
def preOrder(root):
    print(root, end = "")
    if tree[root][0] != ".":
        preOrder(tree[root][0])
    if tree[root][1] != ".":
        preOrder(tree[root][1])
def inOrder(root):
    if tree[root][0] != ".":
        inOrder(tree[root][0])
    print(root, end = "")
    if tree[root][1] != ".":
        inOrder(tree[root][1])   
def postOrder(root):
    if tree[root][0] != ".":
        postOrder(tree[root][0])
    if tree[root][1] != ".":
        postOrder(tree[root][1])
    print(root, end = "")
# Tree 생성(adj_list)
for _ in range(N):
    root, left, right = input().rstrip().split()
    tree[root] = [left, right]
preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
print()