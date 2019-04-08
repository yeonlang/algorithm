

def select(choice,idx,visited,number):
    global myMax
    if choice == 3:
        a,b,c = -1,-1,-1
        for u in range(6):
            if visited[u] and a == -1:
                a = number[u]
                continue
            if visited[u] and b == -1:
                b = number[u]
                continue
            if visited[u] and c == -1:
                c = number[u]

        cnt = abs(a-b)+abs(b-c)+abs(c-a)
        if cnt>myMax:
            myMax = cnt
        return

    for i in range(idx,6):
        visited[i] = 1
        select(choice+1, i+1, visited, number)
        visited[i] = 0

def read(y1,x1,x2):
    n1,n2,n3,n4,n5,n6 = 0,0,0,0,0,0
    for y in range(y1):
        for x in range(x1):
            n1 += data[y][x]

    for y in range(y1):
        for x in range(x1,x2):
            n2 += data[y][x]

    for y in range(y1):
        for x in range(x2,M):
            n3 += data[y][x]

    for y in range(y1,N):
        for x in range(x1):
            n4 += data[y][x]

    for y in range(y1,N):
        for x in range(x1,x2):
            n5 += data[y][x]

    for y in range(y1,N):
        for x in range(x2,M):
            n6 += data[y][x]
    select(0,0,[0,0,0,0,0,0],[n1,n2,n3,n4,n5,n6])

def BTK(c,idx,y1):
    if c == 2:
        x1,x2 = -1,-1
        for u in range(M):
            if visited[u] and x1 == -1:
                x1 = u
                continue
            if visited[u] and x2 == -1:
                x2 = u
                break
        read(y1,x1,x2)
        return

    for x in range(idx,M):
        if not visited[x]:
            visited[x] = 1
            BTK(c+1,x+1,y)
            visited[x] = 0

for tc in range(int(input())):
    N,M = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*M
    myMax = 0
    for y in range(1,N):
        BTK(0,1,y)
    print("#{} {}".format(tc+1,myMax))