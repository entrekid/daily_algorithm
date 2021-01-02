def check(password):
    ja = 0
    mo = 0
    for x in password:
        if x in 'aeiou':
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1

def go(n, alpha, password, i):
    if len(password) == n:
        if check(password):
            print(password)
        return
    if i == len(alpha):
        return
    go(n, alpha, password + alpha[i], i + 1)
    go(n, alpha, password, i + 1)

n, m = map(int, input().split())
a = input().split()
a.sort()
go(n, a, "", 0)