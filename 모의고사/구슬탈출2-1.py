import sys
sys.stdin = open("구슬탈출2.txt")

#공을 보내는 시뮬레이션
def func(ay,ax,by,bx,d):
    #출력값이 pay,pax,pby,pbx이기 때문에
    #공이 갇혔을 경우를 대비해서 미리 들어온 좌표로 초기화 시켜준다.
    pay,pax,pby,pbx = ay,ax,by,bx

    # 다음 방향이 가능하다면
    while not data[ay][ax]:
        # 출발하기전의 위치를 pay,pax에 저장하고
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

# 공의 다음 좌표를 탐색하는 함수
def nxt(ay,ax,by,bx,nowd):
    if (nowd == 0 and ay>by) or (nowd == 1 and bx>ax) or (nowd == 2 and ay<by) or (nowd == 3 and bx<ax):
        by,bx,ay,ax = func(by,bx,ay,ax,nowd)
    else:
        ay,ax,by,bx = func(ay,ax,by,bx,nowd)
    return (ay,ax,by,bx)

def BTK(ay,ax,by,bx,c,pred):
    global cnt,flag
    if c > 10: return
    if cnt != -1 and c>=cnt: return
    for d in range(4):
        if d != pred:
            nay,nax,nby,nbx = nxt(ay,ax,by,bx,d)
            if (nay == findy and nax == findx) and (nby != findy or nbx != findx):
                if c<cnt or cnt == -1:
                    cnt = c
                return
            elif nby==findy and nbx==findx: continue
            BTK(nay,nax,nby,nbx,c+1,d)

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



