L, C = map(int, input().split())
def check(word):
    mo = 0
    ja = 0
    for char in word:
        if char in "aeiou":
            mo += 1
        else:
            ja += 1
    return mo >= 1 and ja >= 2
char_list = list(input().split())
char_list.sort()
ans = []
def go(password, length, idx):
    # 성공한 경우
    if length == L:
        if check(password):
            ans.append(password)
        return
    # 실패한 경우
    if C <= idx:
        return
    # 다음 단계
    else:
        # 현재 idx에 해당하는 문자를 사용
        go(password + char_list[idx], length + 1, idx + 1)
        # 사용하지 않음
        go(password, length, idx + 1)
go("", 0, 0)
for elem in ans:
    print(elem)
