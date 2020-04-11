minkuk = list(map(int, input().split()))
manse = list(map(int, input().split()))
min_sum = sum(minkuk)
man_sum = sum(manse)
if min_sum > man_sum:
    print(min_sum)
else:
    print(man_sum)