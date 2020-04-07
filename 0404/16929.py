import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = [list(input().rstrip()) for _ in range(N)]
print(graph)