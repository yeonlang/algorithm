import sys
sys.stdin = open("미생물.txt","r")

def back(dir):
    if dir == 1: return 2
    elif dir == 2: return 1
    elif dir == 3: return 4
    elif dir == 4: return 3

def sol():
    global result,K

    time = 0
    while time < M:
        judge = {}
        for i in range(K):
            if mito[i]:
                y,x,num,d = mito[i]
                y+=dy[d]
                x+=dx[d]

                if (y,x) in judge:
                    judge[(y,x)]+=1
                else:
                    judge[(y,x)]=1
                mito[i] = (y,x,num,d)

        for key,value in judge.items():
            if value>1:
                y,x = key
                premaxnum,predir,nxtnum = 0,0,0
                for i in range(K):
                    if mito[i] and mito[i][0] == y and mito[i][1] == x:
                        temp = i
                        num,d = mito[i][2],mito[i][3]
                        nxtnum+=num
                        if num > premaxnum:
                            premaxnum = num
                            predir=d
                        mito[i] = 0
                mito[temp] = (y,x,nxtnum,predir)

        for u in range(K):
            if mito[u]:
                y,x,num,d = mito[u]
                if y==0 or y == N-1 or x == 0 or x == N-1:
                    num = num//2
                    if num == 0:
                        mito[u] = 0
                        continue
                    d=back(d)
                    mito[u] = (y,x,num,d)
        v=0
        while v < len(mito):
            if not mito[v]:
                del mito[v]
                continue
            v+=1
        K=len(mito)
        time += 1

    for h in range(K):
        if mito[h]:
            result+=mito[h][2]

for tc in range(int(input())):
    N,M,K = map(int,input().split())
    mito = []
    for i in range(K):
        y,x,num,d = map(int,input().split())
        mito.append((y,x,num,d))

    dx = [0,0,0,-1,1]
    dy = [0,-1,1,0,0]

    result = 0
    sol()
    print("#{} {}".format(tc+1,result))

