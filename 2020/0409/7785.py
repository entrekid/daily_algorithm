import sys
from collections import defaultdict
input = sys.stdin.readline
num = int(input())
stack = defaultdict(int)
name_people = defaultdict(str)
for _ in range(num):
    people, _ = input().rstrip().split()
    name_people[people.lower()] = people
    stack[people.lower()] += 1
ans = []
for key, value in stack.items():
    if value == 2:
        continue
    else:
        ans.append(key)
ans.sort(reverse = True)
for elem in ans:
    print(name_people[elem])
