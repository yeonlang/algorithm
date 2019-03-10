import sys
sys.stdin = open("경사로.txt","r")

for tc in range(int(input())):
    N, X = map(int,input().split())
    data = [ list(map(int,input().split())) for _ in range(N) ]


    for y in range(N):

        # 길이 얼만큼 이어졌는지 판단
        cnt = [0] * N
        # 활주로가 건설되었는지 판단
        visited = [0] * N
        # 활주로를 건설해야 하는 곳 판단.
        check_fly = [0] * N
        for x in range(1,N):
            cnt[x] = cnt[x-1]+1 if data[y][x] == data[y][x-1] else 1
            if data[y][x]-data[y][x-1] > 1: check_fly = 2
            if data[y][x]-data[y][x-1] == 1: check_fly = 1
            if 2 in check_fly:
                break

        for x2 in range(N):
            check












