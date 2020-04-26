import sys
input = sys.stdin.readline
N = int(input())
def check(board):
    ans = -1
    # 행에서 최대 값
    for iter in range(N):
        cnt = 1
        for jter in range(N - 1):
            if board[iter][jter] == board[iter][jter + 1]:
                cnt += 1
            elif board[iter][jter] != board[iter][jter + 1]:
                cnt = 1
            if ans < cnt:
                ans = cnt
    # 열에서 최대 값
    for jter in range(N):
        cnt = 1
        for iter in range(N - 1):
            if board[iter][jter] == board[iter + 1][jter]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
    return ans
board = [list(input().rstrip()) for _ in range(N)]
ans = -1
for iter in range(N):
    for jter in range(N):
        if jter + 1 < N:
            board[iter][jter], board[iter][jter + 1] = board[iter][jter + 1], board[iter][jter]
            temp = check(board)
            board[iter][jter], board[iter][jter + 1] = board[iter][jter + 1], board[iter][jter]
            if temp > ans:
                ans = temp
for jter in range(N):
    for iter in range(N):
        if iter + 1 < N:
            board[iter][jter], board[iter + 1][jter] = board[iter + 1][jter], board[iter][jter]
            temp = check(board)
            board[iter][jter], board[iter + 1][jter] = board[iter + 1][jter], board[iter][jter]
            if temp > ans:
                ans = temp
print(ans)
