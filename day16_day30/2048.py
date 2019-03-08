import sys
sys.stdin = open("2048.txt","r")

def sol(dir):
    if dir == 'up':
        for x in range(N):
            flag = [1] * N
            for y in range(1,N):
                while  0<=y-1<N and data[y-1][x] == 0:
                    data[y-1][x], data[y][x] = data[y][x], data[y-1][x]
                    y-=1
                if 0<=y-1<N and data[y][x] == data[y-1][x] and flag[y-1]:
                    data[y-1][x] = data[y][x] * 2
                    data[y][x] = 0
                    flag[y-1] = 0



    elif dir == 'down':
        for x in range(N):
            flag = [1] * N
            for y in range(N-2,-1,-1):
                while  0<=y+1<N and data[y+1][x] == 0:
                    data[y+1][x], data[y][x] = data[y][x], data[y+1][x]
                    y+=1
                if 0<=y+1<N and data[y][x] == data[y+1][x] and flag[y+1]:
                    data[y+1][x] = data[y][x] * 2
                    data[y][x] = 0
                    flag[y+1] = 0


    elif dir == 'left':
        for y in range(N):
            flag = [1] * N
            for x in range(1, N):
                while 0<=x-1<N and data[y][x-1] == 0:
                    data[y][x-1], data[y][x] = data[y][x], data[y][x-1]
                    x-=1
                if 0<=x-1<N and data[y][x] == data[y][x-1] and flag[x-1]:
                    data[y][x-1] = data[y][x] * 2
                    data[y][x] = 0
                    flag[x-1] = 0


    elif dir == 'right':
        for y in range(N):
            flag = [1] * N
            for x in range(N-2,-1,-1):
                while 0<=x+1<N and data[y][x+1] == 0:
                    data[y][x+1], data[y][x] = data[y][x], data[y][x+1]
                    x+=1
                if 0<=x+1<N and data[y][x] == data[y][x+1] and flag[x+1]:
                    data[y][x+1] = data[y][x] * 2
                    data[y][x] = 0
                    flag[x+1] = 0

for tc in range(int(input())):
    N,dir = input().split()
    N = int(N)
    data = [ list(map(int,input().split())) for _ in range(N) ]

    sol(dir)

    print("#{}".format(tc+1))
    for i in range(N):
        for j in range(N):
            print(data[i][j],end=" ")
        print()



