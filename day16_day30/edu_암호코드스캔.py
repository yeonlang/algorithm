import sys
sys.stdin = open("암호코드스캔.txt","r")

def func(temp):


    t_start = 0
    n = 1

    indata = temp[t_start:t_start+56*n]
    data = [0] * (len(indata) * 4)
    now = 0
    for i in range(len(indata)):

        if indata[i] in judge:
            temp = 10 + judge.index(indata[i])
            for j in range(3, -1, -1):
                data[now] = 1 if temp & 1 << j else 0
                now += 1

        else:
            temp = int(indata[i])
            for j in range(3, -1, -1):
                data[now] = 1 if temp & 1 << j else 0
                now += 1

    start = 0
    while start+56*n<=len(indata):
        cnt = [1] * (7*n) 
        for now in range(start+1, start+56*n):
            cnt[now % (7*n)] = cnt[now % (7*n) - 1] + 1 if indata[now] == indata[now - 1] else 1

            if now % (7*n) == (7*n)-1:
                decoin = [0] * 4
                d = 0
                for idx_t in range((7*n)-1):
                    if cnt[idx_t] >= cnt[idx_t + 1]:
                        decoin[d] = cnt[idx_t]
                        d += 1
                decoin[d] = cnt[-1]
                if deco[decoin[0]][decoin[1]][decoin[2]][decoin[3]] == -1:
                    start+=1
                    continue
                else:
                    pass


judge = ['A', 'B', 'C', 'D', 'E', 'F']
deco = [[[[-1]*5 for _ in range(5)] for _ in range(5)] for _ in range(5)]
deco[3][2][1][1] = 0
deco[2][2][2][1] = 1
deco[2][1][2][2] = 2
deco[1][4][1][1] = 3
deco[1][1][3][2] = 4
deco[1][2][3][1] = 5
deco[1][1][1][4] = 6
deco[1][3][1][2] = 7
deco[1][2][1][3] = 8
deco[3][1][1][2] = 9

for tc in range(int(input())):
    H,W = map(int,input().split())

    judge = ['A', 'B', 'C', 'D', 'E', 'F']
    flag = True
    dataset = set()

    pretemp = []
    for y in range(H):
        temp = list(input())
        if temp == pretemp:
            continue
        pretemp = temp[:]
        for j in temp:
            if j != '0':
                continue
        # temp 는 현재 줄이다.

        func()



