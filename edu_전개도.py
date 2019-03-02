import sys
sys.stdin = open("전개도.txt","r")

def dfs(start):
    global flag,count

    stack = [start]
    while stack:
        y,x = stack.pop()

        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=nx<6 and 0<=ny<6 and data[ny][nx] and not visited[ny][nx]:
                count += 1
                stack.append((ny,nx))
                visited[ny][nx] = 1

    if count != 6:
        flag = False

def judge(now):
    global check,flag
    check = 0
    y,x = now
    x_left = x-2
    x_right = x+2
    y_top = y-2
    y_bottom = y+2
    for i in range(6):
        if x_left>=0 and data[i][x_left]:
            check+=1
        if x_right<6 and data[i][x_right]:
            check+=1
        if y_top>=0 and data[y_top][i]:
            check+=1
        if y_bottom<6 and data[y_bottom][i]:
            check+=1
    if not check:
        flag = False


data = [ list(map(int,input().split())) for _ in range(6)]

point = []
result = []
dx=[1,-1,0,0]
dy=[0,0,-1,1]
visited=[[0]*6 for _ in range(6)]
flag = True
count = 0

for j in range(6):
    for i in range(6):
        if data[j][i] and not visited[j][i]:
            visited[j][i] = 1
            count+=1
            dfs((j,i))

for j in range(6):
    for i in range(6):
        if visited[j][i] :
            judge((j,i))

if flag:
    print("정육면체의 전개도 입니다.")
else:
    print("정육면체의 전개도가 아닙니다.")

