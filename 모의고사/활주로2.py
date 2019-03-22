import sys
sys.stdin = open("활주로.txt")

def read(data):
    global result
    for y in range(N):
        flag = True
        visited = [0]*N
        x = 0
        while x<N-1:
            if abs(data[y][x] - data[y][x+1])>1:
                flag =False
                break
            if data[y][x+1]-data[y][x] == 1:
                temp = x
                for i in range(K):
                    if visited[x] :
                        flag = False
                        break
                    elif x<0:
                        flag = False
                        break
                    else:
                        visited[x] = 1
                        x -= 1
                if flag:
                    x = temp
                else:
                    break
            x+=1
        if not flag:
            continue

        x = N-1
        while 0<=x:
            if data[y][x]-data[y][x-1] == 1:
                temp = x
                for i in range(K):
                    if visited[x]:
                        flag = False
                        break
                    elif x>=N:
                        flag = False
                        break
                    else:
                        visited[x] = 1
                        x += 1
                if flag:
                    x = temp
                else:
                    break
            x-=1
        if not flag:
            continue
        result += 1

for tc in range(int(input())):
    N, K = map(int,input().split())
    data1 = [list(map(int,input().split())) for _ in range(N)]
    data2 = list(zip(*data1))
    result = 0
    read(data1)
    read(data2)
    print("#{} {}".format(tc+1,result))