import sys
sys.stdin = open("재미있는오셀로.txt","r")

def sol():
    global count1,count2
    for y in range(n):
        for x in range(n):
            if data[y][x] == 1 : count1+=1
            elif data[y][x] ==2 : count2+=1

def search(start_y,start_x,dir,find):
    visited = []
    stack=[(start_y,start_x)]
    while stack:
        y,x = stack.pop(0)
        ny = y + dy[dir]
        nx = x + dx[dir]
        if 0<=ny<n and 0<=nx<n:
            if data[ny][nx] :
                stack.append((ny,nx))
                visited.append((ny,nx))
            if data[ny][nx] == find:
                while visited:
                    ty,tx = visited.pop()
                    data[ty][tx] = find
                break

for tc in range(int(input())):
    n,m = map(int,input().split())
    data = [ [0]*n for _ in range(n)]

    temp1=n//2-1
    temp2=n//2

    data[temp1][temp2] = 1
    data[temp2][temp1] = 1
    data[temp1][temp1] = 2
    data[temp2][temp2] = 2


    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]

    count1 = 0
    count2 = 0
    for i in range(m):
        x, y, value = map(int,input().split())
        x-=1
        y-=1

        data[y][x] = value
        for j in range(8):
            search(y,x,j,value)
    sol()
    print("#{} {} {}".format(tc+1,count1,count2))






