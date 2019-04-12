import sys
sys.stdin = open("홈방범서비스.txt")

for tc in range(int(input())):
    N,M = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]

    house = []
    for y in range(N):
        for x in range(N):
            if data[y][x]:
                house.append((y,x))
    maxnum= 0

    for K in range(1,N+2):
        cost = K*K+(K-1)*(K-1)
        for y in range(N):
            for x in range(N):
                cnt = 0
                num = 0
                for hy,hx in house:
                    if abs(hy-y) + abs(hx-x)<K:
                        cnt+=M
                        num+=1
                if cnt>=cost:
                    maxnum = max(maxnum,num)
    print("#{} {}".format(tc+1,maxnum))

