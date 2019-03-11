import sys
sys.stdin = open("블록사목.txt","r")

def push(x):
    global value,maxtop
    data[top[x]][x] = value
    top[x] -= 1
    value = 1 if value == 2 else 2
    maxtop = min(top)

def clean():
    for x in range(6):
        for y in range(top[x]+1,100):
            if y+1<100 and data[y+1][x] == 0:
                data[y][x],data[y+1][x] = data[y+1][x],data[y][x]
                top[x]+=1
        if data[99][x] == 0:
            top[x] = 99

def judge(value):
    global maxtop,score1,score2
    for y in range(maxtop+1,100):
        cntx = [1,1,1,1,1,1]
        for x in range(1,6):
            if data[y][x] == data[y][x-1] and data[y][x-1]:
                temp = cntx[x-1]+1
                cntx[x] = temp
        for now in range(5,-1,-1):
            if cntx[now]>3:
                for i in range(now,now-cntx[now],-1):
                    data[y][i] = 0
                    cntx[i]=1
                    if value == 1:
                        score2 +=1
                    elif value == 2:
                        score1 +=1

for tc in range(int(input())):
    data = [[0]*6 for _ in range(100)]
    top = [99,99,99,99,99,99]
    maxtop = 99
    value = 1
    score1 = 0
    score2 = 0

    for i in map(int,input().split()):
        push(i)
        judge(value)
        clean()
    print(score1)
    print(score2)


