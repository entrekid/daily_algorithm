"""
같은 레벨의 노드는 같은 행에 위치한다.

한 열에는 한 노드만 존재한다.

임의의 노드의 왼쪽 부트리에 있는 노드들은 해당 노드보다 왼쪽의 열에 위치하고,
오른쪽 부트리에 있는 노드들은 해당 노드보다 오른쪽의 열에 위치한다.

노드가 배치된 가장 왼쪽 열과 오른쪽 열 사이엔 아무 노드도 없이 비어있는 열은 없다.

"""
# 행은 트리의 level을 뜻한다.
# 열의 의미는 인오더 방문순서
import sys
input = sys.stdin.readline

N = int(input())
tree = {}
check = [False] * (N + 1)
check[0] = True
for _ in range(N):
    root, *child = input().rstrip().split()
    tree[root] = child
    if child[0] != "-1":
        check[int(child[0])] = True
    if child[1] != "-1":
        check[int(child[1])] = True
for iter in range(1, N + 1):
    if check[iter] == False:
        root = str(iter)
        break
def inorder(root, tree, depth):
    if tree[root][0] != "-1":
        inorder(tree[root][0], tree, depth)
    # root 처리
    if tree[root][1] != "-1":
        inorder(tree[root][1], tree, depth)