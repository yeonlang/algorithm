import sys
sys.stdin = open("CCTV.txt","r")
import copy

def Zcount():
    result=0
    for y in range(n):
        for x in range(m):
            if data[y][x] == 0:
                result += 1
    return result


def fill(y, x, dx, dy, plus):
   for i in range(len(dx)):
       stack = [(y, x)]
       while stack:
           now_y,now_x = stack.pop()

           ny = now_y + dy[i]
           nx = now_x + dx[i]

           if 0<=ny<n and 0<=nx<m and (data[ny][nx] >= 10 or not data[ny][nx]):
               data[ny][nx] += plus
               stack.append((ny,nx))


def search(y, x, value, dir, plus):
    if value == 1:
        fill(y,x,dx1[dir],dy1[dir],plus)
    elif value == 2:
        fill(y, x, dx2[dir], dy2[dir], plus)
    elif value == 3:
        fill(y, x, dx3[dir], dy3[dir], plus)
    elif value == 4:
        fill(y, x, dx4[dir], dy4[dir], plus)
    elif value == 5:
        fill(y, x, dx5[dir], dy5[dir], plus)

def getMin(now):
    global my_min#,scope
    if now == len(cctv):
        now_count = Zcount()
        if now_count < my_min:
            # scope = copy.deepcopy(data)
            my_min = now_count
        return

    y, x, value = cctv[now]
    for i in range(dir_num[value]):
        search(y, x, value, i, 10)
        getMin(now + 1)
        search(y, x, value, i, -10)


n,m = map(int,input().split())
data = [ [0]*m for _ in range(n) ]
dir_num = [0,4,2,4,4,1]
cctv = []
    #상, 하, 좌, 우
dx1 = [[0],[0],[-1],[1]]
dy1 = [[-1],[1],[0],[0]]
    #상하 , 좌우
dx2 = [[0,0],[-1,1]]
dy2 = [[-1,1],[0,0]]
    # 상우, 우하, 하좌, 좌상
dx3 = [[0,1],[1,0],[0,-1],[-1,0]]
dy3 = [[-1,0],[0,1],[1,0],[0,-1]]
    # 좌상우, 상우하, 우하좌, 하좌상
dx4 = [[-1,0,1],[0,1,0],[1,0,-1],[0,-1,0]]
dy4 = [[0,-1,0],[-1,0,-1],[0,1,0],[1,0,-1]]
    # 상하좌우
dx5 = [[0,0,-1,1]]
dy5 = [[-1,1,0,0]]

for y in range(n):
    for x,value in enumerate(map(int,input().split())):
        data[y][x] = value
        if 1<=value<=5:
            cctv.append((y,x,value))

my_min = 1000
temp = Zcount()
if temp < my_min:
    my_min = temp

getMin(0)

print(my_min)

# for i in range(n):
#     print(*scope[i])


