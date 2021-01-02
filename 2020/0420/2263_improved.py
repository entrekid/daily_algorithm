import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
N = int(input())
inorder = input().rstrip().split()
postorder = input().rstrip().split()
position = {}
for idx, elem in enumerate(inorder):
    position[elem] = idx
def solve(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    root = postorder[post_end]
    root_idx = position[root]
    print(root, end = " ")
    # left tree
    in_start_l = in_start
    in_end_l = root_idx - 1
    post_start_l = post_start
    post_end_l = post_start + root_idx - in_start - 1
    solve(in_start_l, in_end_l, post_start_l, post_end_l)
    # right tree
    in_start_r = root_idx + 1
    in_end_r = in_end
    post_start_r = post_start + root_idx - in_start
    post_end_r = post_end - 1
    solve(in_start_r, in_end_r, post_start_r, post_end_r)
solve(0, N - 1, 0, N - 1)
print()