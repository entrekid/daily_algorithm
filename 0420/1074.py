import sys
sys.setrecursionlimit(10 ** 8) 
N, r, c = map(int, input().split())
width = 2 ** N
graph = [[0] * width for _ in range(width)]
cnt = 0
def solve(row, col, width):
    global cnt
    if width == 2:
        for iter in range(2):
            for jter in range(2):
                graph[row + iter][col + jter] = cnt
                if (row + iter) == r and (col + jter) == c:
                    return
                cnt += 1
        return
    width = width // 2
    solve(row, col, width)
    solve(row, col + width, width)
    solve(row + width, col, width)
    solve(row + width, col + width, width)
solve(0, 0, width)
print(graph[r][c])