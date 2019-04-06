import sys
sys.stdin = open("점심식사시간.txt")

def solve(lst,num):
    time = 1
    templst = []
    while lst or templst:
        i = 0
        while i<len(templst):
            templst[i]-=1
            if templst[i] == 0:
                del templst[i]
                continue
            i+=1

        j = 0
        while j<len(lst):
            if time > lst[j] and len(templst)<3:
                del lst[j]
                templst.append(stair[num][2])
                continue
            j+=1
        time+=1

    return time-1

def DFS(c):
    global myMin
    if c == p:
        cnt = max( solve(sorted(result[0]),0) , solve(sorted(result[1]),1) )
        if cnt < myMin:
            myMin = cnt
        return

    for i in range(2):
        temp = abs(people[c][0] - stair[i][0]) + abs(people[c][1] - stair[i][1])
        result[i].append(temp)
        DFS(c+1)
        result[i].pop()

for tc in range(int(input())):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    people = []
    stair = []

    for y in range(N):
        for x in range(N):
            if data[y][x] == 1:
                people.append((y,x))

            elif data[y][x] > 1:
                stair.append((y,x,data[y][x]))

    p = len(people)
    result = [[] for _ in range(2)]
    myMin = 987654321
    DFS(0)

    print("#{} {}".format(tc+1,myMin))



