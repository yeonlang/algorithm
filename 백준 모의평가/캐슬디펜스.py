import sys
sys.stdin = open("궁수.txt")

def array(data):
    global people
    cnt = 0
    for x in range(M):
        for y in range(N-1,0,-1):
            if data[y-1][x]:
                cnt+=1
            data[y][x] = data[y-1][x]
            data[y-1][x] = 0
        data[N-1][x] = 0

    people = set()
    for y in range(N):
        for x in range(M):
            if data[y][x]:
                people.add((y, x))
    if people:
        return False
    else:
        return True

def DFS(c,idx):
    global myMax,people
    if c == 3:
        print(result)
        people = set()
        for y in range(N):
            for x in range(M):
                if data[y][x]:
                    people.add((y, x))
        cnt = 0
        tempdata = [x[:] for x in data]

        while True:
            temp = set()
            for i in range(3):
                yy = N-1
                xx = result[i]
                tempmax = 9999
                ty = 99
                tx = 99
                for py,px in people:
                    val = abs(py-yy)+abs(px-xx)
                    if val<tempmax and val<=D:
                        tempmax = val
                        ty = py
                        tx = px
                    if val == tempmax and px<tx:
                        ty = py
                        tx = px
                if ty == 99 and tx == 99:
                    pass
                else:
                    temp.add((ty,tx))

            cnt += len(temp)
            for i,j in temp:
                tempdata[i][j] = 0
            if array(tempdata):
                break
        if cnt>myMax:
            myMax = cnt
        return

    for x in range(idx,M):
        result[c] = x
        DFS(c+1,x+1)

N,M,D = map(int,input().split())
result = [-1,-1,-1]
data = [list(map(int,input().split())) for _ in range(N)]
data.append([0]*M)
N+=1
myMax = 0
DFS(0,0)
print(myMax)