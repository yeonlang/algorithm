import sys
sys.stdin=open("오목.txt","r")

def judge():
    global visited,issix,resulty,resultx
    count=0
    flag = True
    for i in range(n):
        for j in range(n):
            if visited[j][i]:
                count+=1

    if count == 5:
        for i in range(n):
            for j in range(n):
                if visited[j][i]:
                    if flag:
                        resulty = j
                        resultx = i
                        flag = False
        return True

    return False


def dfs(start,num):
    global visited,result,resulty,resultx
    stack=[start]
    starty,startx=stack.pop()
    for i in range(4):
        visited = [[0] * n for _ in range(n)]
        visited[starty][startx] = 1
        stack=[]
        stack.append((starty,startx))

        while stack:
            y,x = stack.pop()

            for nxt in range(2):
                ny=y+dy[nxt+2*i]
                nx=x+dx[nxt+2*i]
                if 0<=nx<n and 0<=ny<n and data[ny][nx] == num and not visited[ny][nx]:
                    stack.append((ny,nx))
                    visited[ny][nx] = 1

        if judge():
            result=num
            return



n=19
#우,좌 우하,좌상 하,상 좌하,우상
dx=[1,-1, 1,-1, 0, 0,-1, 1]
dy=[0, 0, 1,-1, 1,-1, 1,-1]
visited = [[0] * n for _ in range(n)]
data=[list(map(int,input().split())) for _ in range(n)]
result=0
resulty,resultx = 0,0

for start_y in range(n):
    for start_x in range(n):
        if data[start_y][start_x] == 1:
            dfs((start_y,start_x),1)
            continue
        elif data[start_y][start_x] == 2:
            dfs((start_y,start_x),2)
            continue

if result:
    print(result)
    print(resulty+1,resultx+1)
else:
    print('0')



