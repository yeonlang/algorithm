import sys
sys.stdin = open("치즈.txt","r")

def DFS(start):
    global count
    stack = [start]

    while stack:
        y,x = stack.pop()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=nx<col and 0<=ny<row and not visited[ny][nx]:
                visited[ny][nx] = 1
                if data[ny][nx] == 0:
                    stack.append((ny,nx))
                if data[ny][nx] == 1:
                    count+=1
                    data[ny][nx] = 0


count = 1
result_count = 0
result_time = -1
row, col = map(int, input().split())

data = [ list(map(int,input().split() )) for _ in range(row)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

while count:
    visited = [[0] * col for _ in range(row)]
    visited[0][0]=1
    result_time+=1
    result_count = count
    count=0
    DFS((0,0))

print(result_time)
print(result_count)


