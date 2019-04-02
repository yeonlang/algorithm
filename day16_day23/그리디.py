import sys
sys.stdin = open("그리디.txt")

N,M = map(int,sys.stdin.readline().split())

if N>=3:
    if M >= 7:
        print(M-2)
    elif M <= 4:
        print(M)
    else:
        print(4)
elif N == 1:
    print(1)
else:
    if M >= 8:
        print(4)
    else :
        print((M+1)//2)



