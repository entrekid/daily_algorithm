M = int(input())
N = int(input())
if M < 2:
    print("Before")
elif M == 2:
    if N == 18:
        print("Special")
    elif N < 18:
        print("Before")
    else:
        print("After")
else:
    print("After")