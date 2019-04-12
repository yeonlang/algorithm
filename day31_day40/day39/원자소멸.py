import sys
sys.stdin = open("원자소멸.txt")



dy = [1,-1,0,0]
dx = [0,0,-1,1]
visited = [[0]*4001 for _ in range(4001)]
for tc in range(int(input())):
    minx,miny = 1000,1000
    maxx,maxy = -1000,-1000
    K = int(input())
    data = []
    for _ in range(K):
        x,y,d,power = map(int,input().split())
        minx = min(x,minx)
        miny = min(y,miny)
        maxx = max(x,maxx)
        maxy = max(y,maxy)
        data.append([x,y,d,power])

    N = (maxy-miny)*2
    M = (maxx-minx)*2

    for i in range(K):
        data[i][0]-=minx
        data[i][0] *= 2
        data[i][1]-=miny
        data[i][1] *= 2

    count = 0
    stack1 = []
    stack2 = []

    while data:
        i = 0
        while i<len(data):
            data[i][1] += dy[data[i][2]]
            data[i][0] += dx[data[i][2]]
            if data[i][0]>M or data[i][0]<0 or data[i][1]>N or data[i][1]<0:
                data.pop(i)
                continue
            if visited[data[i][1]][data[i][0]]:
                count += data[i][3]
                stack1.append((data[i][1], data[i][0]))
                data.pop(i)
                continue
            visited[data[i][1]][data[i][0]] = 1
            stack2.append((data[i][1], data[i][0]))
            i+=1

        while stack1:
            y,x = stack1.pop()
            visited[y][x] = 0
            for t in range(len(data)):
                if data[t][0] == x and data[t][1] == y:
                    count += data[t][3]
                    data.pop(t)
                    break

        while stack2:
            y, x = stack2.pop()
            visited[y][x] = 0

    print('#{} {}'.format(tc+1,count))




