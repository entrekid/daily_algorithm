import sys
input = sys.stdin.readline
total = 0
dwarfs = []
for _ in range(9):
    dwarf = int(input())
    dwarfs.append(dwarf)
    total += dwarf
dwarfs.sort()
for iter in range(9):
    for jter in range(iter + 1, 9):
        if total - (dwarfs[iter] + dwarfs[jter]) == 100:
            for kter in range(9):
                if kter != iter and kter != jter:
                    print(dwarfs[kter])
            sys.exit(0)
