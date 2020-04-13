import sys
input = sys.stdin.readline
from collections import Counter

def check(word):
    char_cnt = Counter(word)
    length = len(word)
    for key in char_cnt.keys():
        idx = word.index(key)
        for index in range(idx, idx + char_cnt[key]):
            if word[index] != key:
                return 0
    else:
        return 1

N = int(input())
cnt = 0
for _ in range(N):
    cnt += check(input().rstrip())
print(cnt)