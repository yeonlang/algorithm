import sys
sys.stdin = open("보호필름.txt")

# 약품처리된 셀을 num로 바꿔주는 함수
def select(y,num):
    data[y] = [num]*M

# 성능검사
def read(c):
    global myMin
    for x in range(M):
        cnt = [1]*N
        for y in range(N-1):
            cnt[y+1]= cnt[y]+1 if data[y][x] == data[y+1][x] else 1
            # 성능검사를 통과하였다면 다음 x축 성능검사로 넘어감
            if cnt[y+1]>=K:
                break
            # 하나라도 못 통과하였다면 return
            if y == N-2 and cnt[y+1]<K:
                return
    # 모든셀이 성능검사를 통과하였다면 myMin을 갱신
    if c<myMin:
        myMin = c

def DFS(c,idx,num):
    #약품처리가 원하는 횟수만큼 되었다면 작업 개시
    if c == res:
        # 성능검사를 통과하는지 살펴본다.
        read(c)
        return
    # 약품처리를 해줘야 할 셀을 선택(조합)
    for y in range(idx,N):
        # 약품처리 전 상태를 temp에 저장
        temp = data[y][:]
        # 약품처리 후 다음 약품 처리할 위치를 탐색
        select(y,num)
        DFS(c+1,y+1,num)
        # 다시 약품을 처리하지 않았을 상태로 복귀
        data[y] = temp


for tc in range(int(input())):
    N,M,K = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    myMin = K
    res = 0
    if myMin>1:
        while res <= myMin:
            # 1로 약품처리르 하였을 경우
            DFS(0,0,1)
            if res==myMin: break
            # 0으로 약품처리를 하였을 경우
            DFS(0,0,0)
            res +=1
    else:
        myMin = 0
    print("#{} {}".format(tc+1,myMin))

#1 2
#2 0
#3 4
#4 2
#5 2
#6 0
#7 3
#8 2
#9 3
#10 4
