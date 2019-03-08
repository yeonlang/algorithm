import sys
sys.stdin = open("보호필름.txt","r")

# currentD = D번째 필름을 살펴볼차례 , 약품 처리 횟수 ,
# precnt 지금까지 만족한 특성셀의 수, 각 셀에서 최대한 길게 이어지는 값
def solve(curD, trycnt, precnt, maxprecnt,chemical):
    global my_min
    # 약품 처리횟수가 현재까지의 최소횟수보다 클시 가지치기
    if trycnt >= my_min:
        return
    #내가 보아야 할 필름이 마지막 필름일때
    if curD == D:
        isSatisfied = True
        #0~W까지의 모든셀에 대하여 하나라도 기준을 통과하지 못한다면 not satisfied
        for i in range(W):
            if maxprecnt[i]<K:
                isSatisfied = False
                break
        #모든 셀들이 품질검사를 통과하였고
        #지금까지 조사한 약품 최소 투입수보다 작을시 갱신
        if isSatisfied and trycnt<my_min:
            my_min = trycnt
        return

    for i in range(2,-1,-1):
        chemical[curD] = i
        for j in range(W):
            #cur : 현재상태 prev : 바로 전 상태
            cur = data[curD][j] if chemical[curD] == 2 else chemical[curD]
            prev = data[curD-1][j] if chemical[curD-1] == 2 else chemical[curD-1]

            #만약 현재상태와 전의 상태가 같다면 연속된 셀의 갯수를 +=1
            #다르다면 새롭게 새기 위하여 1로 초기화
            cntnum[j] = precnt[j]+1 if cur == prev else 1

            #가장 많이 연속되는 셀의 갯수를 갱신하여 준다.
            if cntnum[j] > maxprecnt[j]:
                maxcntnum[j] = cntnum[j]
            else:
                maxcntnum[j] = maxprecnt[j]

        #다음 필름을 탐색하러 재귀 출발
        #처리 안했을 시 A약품 처리 A일시 B, B일시 처리 안함( 0 if i ==2 else 1)
        solve(curD+1, trycnt + (0 if i == 2 else 1), cntnum[:], maxcntnum[:],chemical[:])

for tc in range(int(input())):
    D,W,K = map(int, input().split())
    data = [list(map(int,input().split())) for _ in range(D)]

    # 구해야할 최소 투입 횟수
    # 연속해서 K번을 투입할시 무조건 통과가 가능하기때문에 K로 초기화
    my_min = K
    #현재 필름까지 세로방향으로 연속한 동일 특성 셀의 수
    cntnum = [1]*W
    #현재 필름까지 세로 방향으로 연속한 동일 특성 셀의 최대 갯수
    maxcntnum = [1]*W
    #각 셀에 투입된 약품 (A=0,B=1,처리안함=2)
    chemical = [2]*D

    #시작
    #0번셀에 약품 처리를 하지 않을 경우
    solve(1,0,cntnum[:],maxcntnum[:],chemical[:])

    #0번셀에 약품 처리를 A로 하였을 경우
    chemical[0] = 0
    solve(1, 1, cntnum[:], maxcntnum[:],chemical[:])

    #0번셀에 약품 처리를 B로 하였을 경우
    chemical[0] = 1
    solve(1, 1, cntnum[:], maxcntnum[:],chemical[:])

    print(my_min)



