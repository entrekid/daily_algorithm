import sys
input = sys.stdin.readline
def binarySearch(card_list, num):
    left = 0
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        if card_list[mid] == num:
            return 1
        elif card_list[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return 0
N = int(input())
card_list = list(map(int, input().split()))
card_list.sort()
M = int(input())
num_list = list(map(int, input().split()))
for elem in num_list:
    print(binarySearch(card_list, elem), end = " ")
print()