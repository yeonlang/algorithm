import sys
sys.stdin = open("무선충전.txt","r")

def fill(start_y,start_x,D):
    stack = [(start_y,start_x)]
    visited = [ [0]*10 for _ in range(10) ]
    visited[start_y][start_x] = 1
    data[start_y][start_x] = 1

    while stack:
        y,x = stack.pop()

        for i in range(1,5):
            ny = y + dy[i]
            nx = y + dx[i]
            if 0<=nx<10 and 0<=ny<10 and not visited[ny][nx] and visited[y][x] < D :
                stack.append((ny,nx))
                data[ny][nx] += 1
                visited[ny][nx] = visited[y][x] + 1

def sol():
    global result
    time = 0
    while time <= M:
        my_max = 0
        a_judge=[]
        b_judge=[]
        for at_y,at_x,D,P in antenna:
            if abs(a[time][0]-at_y) + abs(a[time][1]-at_x) <= D:
                a_judge.append((at_y,at_x,P))
            if abs(b[time][0]-at_y) + abs(b[time][1]-at_x) <= D:
                b_judge.append((at_y,at_x,P))
        if a_judge and b_judge:
            for i in a_judge:
                for j in b_judge:
                    if not (i[0] == j[0] and i[1] == j[1]):
                        if i[2]+j[2]>my_max:
                            my_max = i[2]+j[2]
                    else :
                        if i[2] > my_max:
                            my_max = i[2]
        elif a_judge:
            for i in a_judge:
                if i[2] > my_max:
                    my_max = i[2]
        elif b_judge:
            for i in b_judge:
                if i[2] > my_max:
                    my_max = i[2]

        result+=my_max
        time+=1

for tc in range(int(input())):
    M,N = map(int,input().split())

    data = [ [0]*10 for _ in range(10) ]
    antenna = []
    #상우하좌
    dy=[0,-1,0,1,0]
    dx=[0,0,1,0,-1]

    a=[(0,0)]
    b=[(9,9)]

    for i in range(2):
        if i == 0:
            for j,nxt in enumerate(map(int,input().split())):
                ny = a[j][0] + dy[nxt]
                nx = a[j][1] + dx[nxt]
                a.append((ny,nx))

        else:
            for j,nxt in enumerate(map(int,input().split())):
                ny = b[j][0] + dy[nxt]
                nx = b[j][1] + dx[nxt]
                b.append((ny,nx))

    for i in range(N):
        ap_x, ap_y, D, P = map(int,input().split())
        antenna.append((ap_y-1,ap_x-1,D,P))

    result = 0
    sol()
    print("#{} {}".format(tc+1,result))



