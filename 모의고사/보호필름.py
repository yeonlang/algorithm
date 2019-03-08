import sys
sys.stdin = open("보호필름.txt","r")

from itertools import permutations,product

def solve(curD, chemicalcnt, cntnum, maxcntnum):
    global my_min
    if chemicalcnt >= my_min:
        return

    if curD == D:
        isSatisfied = True
        for i in range(W):
            if cntnum<K:
                isSatisfied = False
                break

        if isSatisfied and chemicalcnt<my_min:
            my_min = chemicalcnt
            return


for tc in range(int(input())):
    D,W,K = map(int, input().split())
    data = [list(map(int,input().split())) for _ in range(N)]

    my_min = K
    cntnum = [0]*20
    maxcntnum = [0]*20
    chemical = [0] * 13

    #1로 초기화
    for i in range(W):
        cntnum[i] = 1
        maxcntnum[i] = 1

    chemical[0] = 2
    solve(1,0,cntnum,maxcntnum)

    chemical[0] = 0
    solve(1, 1, cntnum, maxcntnum)

    chemical[0] = 1
    solve(1, 1, cntnum, maxcntnum)




