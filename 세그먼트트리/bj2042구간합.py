import sys
sys.stdin = open("구간합.txt","r")

def update(a,b):
    where = base +a -1
    IDT[where] = b
    where >>= 1

    while where:
        IDT[where] = IDT[where*2]+IDT[where*2+1]
        where >>=1


def RSQ(ffrom, to):
    ffrom = ffrom + base-1
    to = to + base -1
    ssum =0

    while ffrom < to:
        if ffrom&1:
            ssum+= IDT[ffrom]
            ffrom += 1
        if not to%2:
            ssum+= IDT[to]
            to -= 1
        ffrom >>= 1
        to >>=1

    if ffrom == to :
        ssum += IDT[ffrom]
    print(ssum)


N,M,K = map(int,input().split())
base = 1
while base <= N:
    base <<= 1
IDT = [0]*(base*2)

for now in range(base, N + base):
    IDT[now] = int(input())

for parent in range(base-1, 0, -1):
    IDT[parent] = IDT[parent*2]+IDT[parent*2+1]

for i in range(M+K):
    a,b,c = map(int,input().split())
    if a == 1:
        update(b,c)
    else:
        RSQ(b,c)