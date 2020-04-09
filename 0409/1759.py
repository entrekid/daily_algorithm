import sys
L, C = map(int, input().split())
str_list = list(input().rstrip().split())
str_list.sort()
length = len(str_list)
result = []
def check(word):
    vowel = False
    other = False
    cnt = 0
    for character in word:
        if character in ["a", "e", "i" ,"o", "u"]:
            vowel = True
        else:
            cnt += 1
        
        if cnt == 2:
            other = True
        
        if other and vowel:
            return True

    else:
        return False
def go(L, C, index, base):
    if index == L:
        if check(result):
            print("".join(result))
            return
        else:
            return
    else:
        for iter in range(base, length):
            result.append(str_list[iter])
            go(L, C, index + 1, iter + 1)
            result.pop()
go(L, C, 0, 0)