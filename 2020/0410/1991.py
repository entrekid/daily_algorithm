import sys
input = sys.stdin.readline
N = int(input())
preorder_st = []
inorder_st = []
postorder_st = []

def preorder(root, tree):
    preorder_st.append(root)
    if tree[root][0] != ".":
        preorder(tree[root][0], tree)
    if tree[root][1] != ".":
        preorder(tree[root][1], tree)

def inorder(root, tree):
    if tree[root][0] != ".":
        inorder(tree[root][0], tree)
    inorder_st.append(root)
    if tree[root][1] != ".":
        inorder(tree[root][1], tree)

def postorder(root, tree):
    if tree[root][0] != ".":
        postorder(tree[root][0], tree)
    if tree[root][1] != ".":
        postorder(tree[root][1], tree)
    postorder_st.append(root)

tree = {}
for _ in range(N):
    root, *info = input().rstrip().split()
    tree[root] = info
preorder("A", tree)
inorder("A", tree)
postorder("A", tree)
print("".join(preorder_st))
print("".join(inorder_st))
print("".join(postorder_st))