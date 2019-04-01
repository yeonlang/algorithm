import sys
sys.stdin = open("탈주범검거.txt","r")

def judge(y,x,originy,originx):
    for i in range(dir_num[data[y][x]]):
        ny = y + dy[data[y][x]][i]
        nx = x + dx[data[y][x]][i]
        if ny == originy and nx == originx:
            return True
    return False

def search(y,x):
    que = [(y,x)]
    while que:
        y,x = que.pop(0)
        for i in range(dir_num[data[y][x]]):
            ny = y + dy[data[y][x]][i]
            nx = x + dx[data[y][x]][i]
            if 0<=ny<n and 0<=nx<m and judge(ny,nx,y,x) and not visited[ny][nx]:
                visited[ny][nx] = visited[y][x]+1
                if visited[ny][nx] > K:
                    return
                que.append((ny,nx))

def solution():
    count=0
    for y in range(n):
        for x in range(m):
            if 0<visited[y][x]<=K:
                count+=1
    return count

for tc in range(int(input())):
    n,m,start_y,start_x,K = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]

    dir_num = [0,4,2,2,2,2,2,2]
             #상하좌우,   상하,   좌우,    상우,   우하,   하좌,   좌상
    dx = [0,[0, 0, -1, 1],[0, 0], [-1, 1],[0, 1], [1, 0], [0, -1], [-1, 0]]
    dy = [0,[-1, 1, 0, 0],[-1, 1], [0, 0],[-1, 0], [0, 1], [1, 0], [0, -1]]

    visited[start_y][start_x] = 1
    search(start_y,start_x)

    print("#{} {}".format(tc+1,solution()))

