N = int(input())
inorder = input().split()
postorder = input().split()
position = [-1] * (N + 1)
for idx, elem in enumerate(inorder):
    position[int(elem)] = idx
def solve(in_start, postorder):
    if not inorder and not postorder:
        return
    root = postorder[-1]
    root_idx = position[root]
    root_idx = inorder.index(root)
    left_inorder = inorder[ : root_idx]
    left_postorder = postorder[ : root_idx]
    right_inorder = inorder[root_idx + 1 : ]
    right_postorder = postorder[root_idx : -1]
    print(root, end = " ")
    solve(left_inorder, left_postorder)
    solve(right_inorder, right_postorder)
solve(inorder, postorder)
print()