import sys
sys.stdin = open("줄기세포.txt","r")

# alive를 1씩 줄이고 다음 후보군
def func1():
    count = 0
    for y in range(ln):
        for x in range(lm):
            if alive[y][x] and alive[y][x] <= data[y][x]:
                stack.append((y, x, data[y][x]))
            if alive[y][x] :
                alive[y][x]-=1
            if alive[y][x] :
                count+=1
    return count

#줄기세포의 상태를 변화
def search():
    count = 0
    while stack:
        y,x,value = stack.pop()

        for nxt in range(4):
            ny=y+dy[nxt]
            nx=x+dx[nxt]
            if not data[ny][nx]:
                count+=1
                data[ny][nx] = value
                alive[ny][nx] = 2*value
    return count



for tc in range(int(input())):
    N, M, K = map(int,input().split())
    offset = K//2+1
    lm = M+2*offset
    ln = N+2*offset

    data = [ [0]*lm for _ in range(ln) ]
    alive = [ [0]*lm for _ in range(ln) ]

    for i in range(N):
        for j,num in enumerate(map(int,input().split())):
            data[offset+i][offset+j] = num
            alive[offset+i][offset+j] = 2*num

    #상하좌우
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    stack = []
    time = 0
    while time != K:
        l = func1()
        if stack:
            stack.sort(key=lambda x: x[2], reverse = True)
            result = search()

        time += 1
    if l == result:
        l = 0
    print("#{} {}".format(tc+1,result+l))
