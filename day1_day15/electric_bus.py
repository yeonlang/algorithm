import sys
sys.stdin = open('electric_bus.txt', 'r') #파일에서 읽을때 사용

for tc in range(int(input())):
    move, N, M = map(int,input().split())
    lst= list(map(int,input().split()))

    #충전소가 있다면 0 없다면 -1인 count 초기화
    count = [-1]*(N+1)
    count[0] = 0
    for i in lst:
        count[i]+=1

    #방문위치를 담을 queue
    que=[]

    #첫 방문위치를 담는다.
    for j in range(N-1,N-move-1,-1):
        if count[j] == 0:
            que.append(j)
            count[j]+=1

    #BFS
    while que:
        start = que.pop(0)
        end = start - move

        #첫번째 인덱스에 도달할 경우 while 문을 빠져나가는 코드
        if start == 0:
            #결과값은 첫번째 충전소도 포함하는 까닭에 시작값-1
            count[start]-=1
            break

        #카운트 탐색인덱스가 0보다 적어지지 않도록 초기화
        if end<0:
            end=0

        for k in range(start-1,end-1,-1):
            #방문하지 않았다면 방문
            if count[k]==0:
                #다음 방문위치
                que.append(k)
                #현재위치에 도달하는 시간 = 이전위치도달시간 +1
                count[k] = count[start]+1

    print(f"#{tc+1} {count[0]}")






