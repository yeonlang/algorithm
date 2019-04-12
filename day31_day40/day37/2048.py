import sys
sys.stdin = open("2048.txt")

def turnright(data):
    tp = [[0]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            tp[y][x] = data[N-x-1][y]
    return tp

def turnleft(data):
    tp = [[0]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            tp[N-x-1][y] = data[y][x]
    return tp

def left(data):
    return turnright(turnright(right(turnright(turnright(data)))))

def right(data):
    for y in range(N):
        tp1 = []
        for x in range(N):
            if data[y][x]:
                tp1.append(data[y][x])
                data[y][x] = 0
        for i in range(len(tp1)-1,0,-1):
            if tp1[i] == tp1[i-1]:
                tp1[i] = tp1[i]*2
                tp1[i-1] = 0
        i = 0
        while i<len(tp1):
            if not tp1[i]:
                tp1.pop(i)
                continue
            i+=1

        x = N-1
        while tp1:
            data[y][x] = tp1.pop()
            x-=1
    return data

def up(data):
    return turnleft(right(turnright(data)))


def down(data):
    return turnright(right(turnleft(data)))

def findmax(data):
    m = 0
    for y in range(N):
        for x in range(N):
            m = max(data[y][x],m)
    return m

def DFS(c):
    global myMax
    if c == 5:
        temp = [x[:] for x in data]
        for i in result:
            if i == 0:
                temp = right(temp)
            elif i == 1:
                temp = down(temp)
            elif i == 2:
                temp = left(temp)
            elif i == 3:
                temp = up(temp)
        tp = findmax(temp)
        if tp > myMax:
            myMax = tp
        return

    for i in range(4):
        result[c] = i
        DFS(c+1)

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
result = [0,0,0,0,0]
myMax = 0
DFS(0)
print(myMax)
