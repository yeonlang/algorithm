import sys
sys.stdin = open("탈주범검거.txt","r")

# 내가 갈 다음위치에서 원래위치로 돌아올 수 있는지 탐색하는 함수
def judge(y,x,originy,originx):
    # 다음위치에서 이동할 수 있는칸에
    for i in range(dir_num[data[y][x]]):
        ny = y + dy[data[y][x]][i]
        nx = x + dx[data[y][x]][i]
        # 원래의 칸이 있다면 return True 아니면 False
        if ny == originy and nx == originx:
            return True
    return False

#BFS
def search(sy,sx):
    que = [(sy,sx)]
    visited[sy][sx] = 1
    while que:
        y,x = que.pop(0)
        for i in range(dir_num[data[y][x]]):
            ny = y + dy[data[y][x]][i]
            nx = x + dx[data[y][x]][i]
            # 다음 좌표가 범위 안에 위치하고, 다음 위치에 방문도 가능하며, 지금까지 방문하지 않았다면
            if 0<=ny<n and 0<=nx<m and judge(ny,nx,y,x) and not visited[ny][nx]:
                visited[ny][nx] = visited[y][x]+1
                # 거리가 K보다 커진다면 return
                if visited[ny][nx] > K:
                    return
                que.append((ny,nx))

# visited를 탐색하며 방문한 위치들을 count에 더해준다.
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

    # 파이프 번호에 따른 이동방향 배열로 구현
    dir_num = [0,4,2,2,2,2,2,2]
             #상하좌우,   상하,   좌우,    상우,   우하,   하좌,   좌상
    dx = [0,[0, 0, -1, 1],[0, 0], [-1, 1],[0, 1], [1, 0], [0, -1], [-1, 0]]
    dy = [0,[-1, 1, 0, 0],[-1, 1], [0, 0],[-1, 0], [0, 1], [1, 0], [0, -1]]

    search(start_y,start_x)
    print("#{} {}".format(tc+1,solution()))

