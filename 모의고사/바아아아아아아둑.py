import sys
sys.stdin = open("바아아아아아아둑.txt")

def ispass(y,x): return True if 0<=y<N and 0<=x<M else False
def BFS():
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for start_y in range(N):
        for start_x in range(M):
            if not visited[start_y][start_x] and not data[start_y][start_x]:
                que = [(start_y,start_x)]
                visited[start_y][start_x] = 1
                while que:
                    y,x = que.pop()
                    for i in range(4):
                        ny = y+dy[i]
                        nx = x+dx[i]
                        if ispass(ny,nx) and data[ny][nx] != 1 and not visited[ny][nx]:
                            if data[ny][nx]: cnt+=1
                            visited[ny][nx] = 1
                            que.append((ny,nx))
    return len(player2)-cnt


def select(choice,idx):
    global myMax

    if choice == 2:
        temp = BFS()
        if temp > myMax:
            myMax = temp
        return

    for i in range(idx,N*M):
        if not data[i//M][i%M]:
            data[i//M][i%M] = 1
            select(choice+1,i+1)
            data[i//M][i%M] = 0

dy = [-1,0,1,0]
dx = [0,1,0,-1]

N,M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
player2 = []
for y in range(N):
    for x in range(M):
        if data[y][x] == 2:
            player2.append((y,x))

myMax = 0
select(0,0)
print(myMax)