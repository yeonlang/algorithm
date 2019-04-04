import sys
sys.stdin = open("2048.txt")

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
            while 0<i:
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
                i += 1

            y = 0
            while temp:
                data[y][x] = temp.pop(0)
                y += 1

for tc in range(int(input())):
    N, d = input().split()
    N = int(N)
    if d == 'up': d = 3
    elif d == 'down': d = 1
    elif d == 'right': d = 0
    elif d == 'left': d = 2
    data = [list(map(int,input().split())) for _ in range(N)]
    turn(data,d)
    print("#%d"%(tc+1))
    for i in range(N):
        print(*data[i])