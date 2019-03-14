import sys
sys.stdin = open("indextree.txt","r")

IDT = [0]*(1<<5)
data = list(map(int,input().split()))
harmony = len(data)

def updata(a,b):
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

base = 1
while base < harmony:
    base <<= 1
