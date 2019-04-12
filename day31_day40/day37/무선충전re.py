import sys
sys.stdin = open("무선충전.txt")


dy = [0,-1,0,1,0]
dx = [0,0,1,0,-1]

for tc in range(int(input())):
    T, N = map(int,input().split())
    dirA = list(map(int,input().split()))
    dirB = list(map(int,input().split()))
    ay,ax = 0,0
    by,bx = 9,9

    charger = []
    for _ in range(N):
        x,y,c,p = map(int,input().split())
        x-=1
        y-=1
        charger.append((y,x,c,p))

    charger.sort(key = lambda x:x[3], reverse=True)
    C = len(charger)
    t = 0
    result = 0
    while True:
        cntlstA = [0]*C
        cntlstB = [0]*C
        for i in range(C):
            if abs(ay - charger[i][0]) + abs(ax-charger[i][1]) <= charger[i][2]:
                cntlstA[i]+=1
            if abs(by - charger[i][0]) + abs(bx-charger[i][1]) <= charger[i][2]:
                cntlstB[i]+=1
        check = 0
        A = 0
        B = 0
        for j in range(C):
            if not A and cntlstA[j] and not cntlstB[j]:
                result+=charger[j][3]
                A+=1
            if not B and cntlstB[j] and not cntlstA[j]:
                result += charger[j][3]
                B+=1
            if cntlstA[j] and cntlstB[j]:
                result += charger[j][3]
                check+=1
            if A+B+check>=2:
                break
        if t>=T:
            break
        ay += dy[dirA[t]]
        ax += dx[dirA[t]]
        by += dy[dirB[t]]
        bx += dx[dirB[t]]
        t+=1
    print('#{} {}'.format(tc+1,result))






