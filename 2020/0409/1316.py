import sys
input = sys.stdin.readline
n = int(input())
def cnt(word):
    character = set(word)
    
ans = 0
for _ in range(n):
    ans += cnt(input())
print(ans)