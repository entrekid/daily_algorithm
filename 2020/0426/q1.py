import sys
input = sys.stdin.readline
def main():
    num = int(input())
    num_list = list(map(int, input().rstrip().split()))
    dp_list = [0] * num
    dp_list[0] = num_list[0]
    for iter in range(1, num):
        dp_list[iter] = max(dp_list[iter - 1] + num_list[iter], num_list[iter])
    print(max(dp_list))
    return
main()