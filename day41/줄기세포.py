import sys
sys.stdin = open("줄기세포.txt")

def read():
    for y in range(N):
        for x in range(M):
            if energy[y][x]:
                energy[y][x] -= 1
            if energy[y][x] and energy[y][x] == data[y][x]:
                spread[data[y][x]].append((y,x))
def fill():
    for num in range(10,0,-1):
        while spread[num]:
            y,x = spread[num].pop()
            for dy,dx in (1,0),(-1,0),(0,1),(0,-1):
                ny = y+dy
                nx = x+dx
                if not data[ny][nx]:
                    data[ny][nx] = num
                    energy[ny][nx] = num*2+1
                    
data = [[0]*701 for _ in range(701)]
energy = [[0]*701 for _ in range(701)]
N,M = 701,701
for tc in range(int(input())):
    spread = [[] for _ in range(11)]
    ln,lm,K = map(int,input().split())
    temp = [list(map(int,input().split())) for _ in range(ln)]
    for y in range(ln):
        for x in range(lm):
            if temp[y][x]:
                data[y+K][x+K] = temp[y][x]
                energy[y+K][x+K] = temp[y][x]*2+1

    time = 1
    while time <= K:
        read()
        fill()
        time+=1

    read()
    cnt = 0
    for y in range(N):
        for x in range(M):
            if energy[y][x]:
                cnt+=1
            energy[y][x] = data[y][x] = 0

    print("#{} {}".format(tc+1,cnt))












