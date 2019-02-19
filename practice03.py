import sys
sys.stdin=open('practice03.txt', 'r')

#이차원 리스트를 받아 최소값을 리턴함과 동시에 리스트에서 삭제
def Low(lst):
    my_min = len(lst)**2+1
    a,b = 0 ,0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j]<my_min:
                my_min=lst[i][j]
                a,b=i,j
    return lst[a].pop(b)

#갈수 있는 지역인지 없는 지역인지 판단하는 함수
def Pass(y,x,n):
    L,B,R,T =nxt//4, (nxt+1)//4, (nxt+2)//4, (nxt+3)//4
    if L<=x<n-R and T<=y<n-B:
        return True
    else:
        return False

#현재의 좌표, nxt=꺽어진횟수, count=새로운입력을 추가한 횟수
x, y, nxt, count = 0, 0, 0, 0

#우 하 좌 상
dx=[1,0,-1,0]
dy=[0,1,0,-1]

#인풋을 받아와 이차원리스트를 생성해준다.
lst=[]
lst.append(list(map(int,input().split())))

#이차원 배열의 크기 = V, 한 행의 원소갯수 = n
n=len(lst[0])
V=n**2
for _ in range(n-1):
    lst.append(list(map(int,input().split())))
arr=[ [0]*n for _ in range(n)]


while count<V:
    #입력으로 받은 이차원 배열의 최소값과 최소값의 인덱스(j,i)를 가져온다.

    #다음 좌표가 갈 수 있는 곳이라면
    if Pass(y,x,n):
        #다음 좌표가 가리키는 공간에 최소값 저장
        arr[y][x]=Low(lst)

    else:
        #다음 좌표가 갈 수 없는 곳이라면 다음좌표를 이전좌표로 초기화 count-=1
        x -= dx[nxt % 4]
        y -= dy[nxt % 4]
        count-=1
        #갈수없는 곳에 도달하였기 때문에 한번 꺽어준다.
        nxt += 1

    #좌표를 다음 좌표로 갱신해준다, count+=1
    x+=dx[nxt%4]
    y+=dy[nxt%4]
    count+=1

for _ in range(n):
    print(arr[_])




