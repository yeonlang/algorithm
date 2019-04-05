import sys
sys.stdin = open("벌꿀채취.txt")


def solve(c,idx,result,data):
    global tempMax
    if result:
        cnt = 0
        cntsum = 0
        for j in result:
            cnt += data[j]
            cntsum += data[j]**2
        if cnt>C:
            return
        if cntsum>tempMax:
            tempMax = cntsum

    for i in range(idx,M):
        result.append(i)
        solve(c+1,idx+1,result,data)
        result.pop()

def DFS(c,idx):
    global tempMax,myMax
    if c == 2:
        cnt = 0
        tempMax = 0
        y1 = result[0]
        for x1 in range(N-M+1):
            solve(0,0,[],data[y1][x1:x1+M])
        cnt += tempMax

        tempMax = 0
        y2 = result[1]
        for x2 in range(N-M+1):
            solve(0,0,[],data[y2][x2:x2+M])
        cnt += tempMax

        if cnt>myMax:
            myMax = cnt
        return

    for i in range(idx,N):
        result[c] = i
        DFS(c+1,i+1)
        result[c] = 0


for tc in range(int(input())):
    N,M,C = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    result = [0,0]
    myMax = 0
    DFS(0,0)
    print(myMax)

    # 1 174
    # 2 131
    # 3 145
    # 4 155
    # 5 166
    # 6 239
    # 7 166
    # 8 172
    # 9 291
    # 10 464
