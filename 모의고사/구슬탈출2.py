import sys
sys.stdin = open("구슬탈출2.txt")

def func(ay,ax,by,bx,d):
    pay,pax,pby,pbx = ay,ax,by,bx
    while not data[ay][ax]:
        pay, pax = ay, ax
        ay += dy[d]
        ax += dx[d]
        if ay == findy and ax == findx:
            pay,pax = findy,findx
            break
    data[pay][pax] = 7
    while not data[by][bx]:
        pby, pbx = by, bx
        by += dy[d]
        bx += dx[d]
        if by == findy and bx == findx:
            pby,pbx = findy,findx
            break
    data[pay][pax] = 0
    return (pay,pax,pby,pbx)

def nxt(ay,ax,by,bx,nd):
    # 위로
    if nd == 0:
        if ay>by:
            a,b,c,d = func(by,bx,ay,ax,nd)
            return (c,d,a,b)
        else:
            a,b,c,d = func(ay,ax,by,bx,nd)
            return (a,b,c,d)
    # 우로
    if nd == 1:
        if bx>ax:
            a,b,c,d = func(by,bx,ay,ax,nd)
            return (c,d,a,b)
        else:
            a,b,c,d = func(ay,ax,by,bx,nd)
            return (a,b,c,d)
    # 하로
    if nd == 2:
        if ay<by:
            a,b,c,d = func(by,bx,ay,ax,nd)
            return (c,d,a,b)
        else:
            a,b,c,d = func(ay,ax,by,bx,nd)
            return (a,b,c,d)
    # 좌로
    if nd == 3:
        if bx<ax:
            a,b,c,d = func(by,bx,ay,ax,nd)
            return (c,d,a,b)
        else:
            a,b,c,d = func(ay,ax,by,bx,nd)
            return (a,b,c,d)

def BTK(ay,ax,by,bx,c,pred):
    global cnt,flag
    if c > 10: return
    if c>=cnt and cnt != -1: return
    for i in range(4):
        if i != pred:
            nay,nax,nby,nbx = nxt(ay,ax,by,bx,i)
            if (nay == findy and nax == findx) and (nby != findy or nbx != findx):
                if c<cnt or cnt == -1:
                    cnt = c
                return
            elif nby==findy and nbx==findx: continue
            BTK(nay,nax,nby,nbx,c+1,i)

dy = [-1,0,1,0]
dx = [0,1,0,-1]
N,M = map(int,input().split())
data = [[0]*M for _ in range(N)]
for y in range(N):
    for x,value in enumerate(input()):
        if value == '#': data[y][x] = 1
        elif value == '.': continue
        elif value == 'O': findy,findx = y,x
        elif value == 'R':
            R = [y,x]
        elif value == 'B':
            B = [y,x]
flag = True
cnt = -1
BTK(R[0],R[1],B[0],B[1],1,-1)
print(cnt)



