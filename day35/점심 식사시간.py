import sys
sys.stdin = open("점심 식사시간.txt")

def DFS(c,maxcnt):
    global myMin
    if maxcnt>=myMin: return
    tempcnt = 0
    for i in range(s):
        tempdata = sorted(result[i])
        temp = []
        time = 1
        while tempdata or temp:
            u = 0
            while u<len(temp):
                temp[u] -= 1
                if temp[u]==0:
                    del temp[u]
                    continue
                u += 1

            j = 0
            while j<len(tempdata):
                if time>=tempdata[j] and len(temp)<3:
                    temp.append(Stair[i][2])
                    del tempdata[j]
                    continue
                j += 1
            time += 1
        time -= 1
        tempcnt =time if time>tempcnt else tempcnt

    if c == p:
        if tempcnt < myMin:
           myMin = tempcnt
        return

    for i in range(s):
        result[i].append(abs(People[c][0]-Stair[i][0]) + abs(People[c][1]-Stair[i][1])+1)
        DFS(c+1,tempcnt)
        result[i].pop()

for tc in range(int(input())):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    People = []
    Stair = []
    for y in range(N):
        for x in range(N):
            if data[y][x] == 1:
                People.append((y,x))
            elif data[y][x]>1:
                Stair.append((y,x,data[y][x]))
    p = len(People)
    s = len(Stair)
    result = [[] for _ in range(s)]
    myMin = 987654321
    DFS(0,0)
    print("#{} {}".format(tc+1,myMin))

#1 9
#2 8
#3 9
#4 7
#5 8
#6 8
#7 11
#8 11
#9 18
#10 12



