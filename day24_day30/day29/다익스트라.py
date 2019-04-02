import sys
sys.stdin = open("다익스트라.txt")

def func():
    cnt = 987654321
    for i in range(N):
        if distance[i][0]<cnt and not distance[i][1]:
            cnt = i
    if cnt == 987654321:
        return (0, True)
    return (cnt, False)

N,M = map(int,input().split())
myMap = [[0]*N for _ in range(N)]
distance = [[987654321,0,''] for _ in range(N)]
for i in range(M):
    y,x,value = map(int,input().split())
    myMap[y][x] = value
start = 0
distance[start][0] = 0

while True:
    now,flag = func()
    if flag: break
    distance[now][1] = 1
    for nxt in range(N):
        if myMap[now][nxt]:
            temp = distance[now][0]+myMap[now][nxt]
            if temp<distance[nxt][0]:
                distance[nxt][0] = temp
                distance[nxt][2] = distance[now][2] + str(now+1) + ' '


for j in range(N):
    print(j+1,distance[j][0],' '+distance[j][2]+str(j+1))


