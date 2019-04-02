import sys
sys.stdin = open("2048.txt")

import copy

def turn(data,d):
    # 우 하 좌 상
    if d == 0:
        for y in range(N):
            temp = []
            for x in range(N):
                if data[y][x]:
                    temp.append(data[y][x])
                    data[y][x] = 0

            i = len(temp)-1
            while 0<=i:
                if temp[i] == temp[i-1]:
                    temp[i] = temp[i]+temp[i-1]
                    del temp[i-1]
                    i-=1
                i-=1

            x = N-1
            while temp:
                data[y][x] = temp.pop()
                x-=1

    elif d == 1:
        for x in range(N):
            temp = []
            for y in range(N):
                if data[y][x]:
                    temp.append(data[y][x])
                    data[y][x] = 0

            i = len(temp)-1
            while 0 < i:
                if temp[i] == temp[i-1]:
                    temp[i] = temp[i] + temp[i-1]
                    del temp[i-1]
                    i -= 1
                i -= 1

            y = N-1
            while temp:
                data[y][x] = temp.pop()
                y -= 1

    elif d == 2:
        for y in range(N):
            temp = []
            for x in range(N):
                if data[y][x]:
                    temp.append(data[y][x])
                    data[y][x] = 0

            i = 0
            while i<len(temp)-1:
                if temp[i] == temp[i+1]:
                    temp[i] = temp[i] + temp[i+1]
                    del temp[i+1]
                    i+=1
                i += 1

            x = 0
            while temp:
                data[y][x] = temp.pop(0)
                x += 1

    elif d == 3:
        for x in range(N):
            temp = []
            for y in range(N):
                if data[y][x]:
                    temp.append(data[y][x])
                    data[y][x] = 0
            i = 0
            while i < len(temp) - 1:
                if temp[i] == temp[i+1]:
                    temp[i] = temp[i] + temp[i+1]
                    del temp[i+1]
                    i+=1
                i += 1

            y = 0
            while temp:
                data[y][x] = temp.pop(0)
                y += 1

def nxtmap(Map,d):
    data = copy.deepcopy(Map)
    turn(data,d)
    return data


def BTK(c,data):
    global myMax
    if c == 5:
        cnt = 0
        for y in range(N):
            for x in range(N):
                if data[y][x]>cnt:
                    cnt = data[y][x]

        if cnt>myMax:
            myMax = cnt
        return

    for i in range(4):
        BTK(c+1,nxtmap(data,i))

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
myMax = 0
BTK(0,data)

print(myMax)