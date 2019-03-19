import sys
sys.stdin = open("암호코드스캔.txt","r")

dic = {
    '0': '0000',    '1': '0001',    '2': '0010',    '3': '0011',    '4': '0100',    '5': '0101',
    '6': '0110',    '7': '0111',    '8': '1000',    '9': '1001',    'A': '1010',    'B': '1011',
    'C': '1100',    'D': '1101',    'E': '1110',    'F': '1111'}
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

def func():
    value = [0] * 8
    result = 0
    idx = 7

    for y in range(N):
        x = M - 1
        while x >= 0:
            if data[y][x] != '0' and data[y - 1][x] == '0':
                cntlst = [0, 0, 0, 0]
                idx_cnt = 3
                sample = dic[data[y][x]]
                start = 3
                cnt = 0
                pre = '1'

                while sample[start] == '0':
                    start-=1

                while cntlst[0] == 0:
                    now = sample[start]
                    if now == pre:
                        cnt+=1
                        start-=1
                    else:
                        cntlst[idx_cnt]=cnt
                        idx_cnt-=1
                        cnt = 1
                        pre = now
                        start-=1
                        if idx_cnt == -1:
                            mmin = min(cntlst)
                            cntlst[0], cntlst[1], cntlst[2], cntlst[3] = cntlst[0] // mmin, cntlst[1] // mmin, cntlst[2] // mmin, cntlst[3] // mmin
                            value[idx] = deco[cntlst[0]][cntlst[1]][cntlst[2]][cntlst[3]]
                            cntlst = [0, 0, 0, 0]
                            idx_cnt = 3
                            idx -= 1
                    if start == -1 :
                        x-=1
                        sample = dic[data[y][x]]
                        if idx == 0 and idx_cnt == 0:
                            cntlst[idx_cnt]=cnt
                            mmin = min(cntlst[1:])
                            cntlst[1], cntlst[2], cntlst[3] = cntlst[1] // mmin, cntlst[2] // mmin, cntlst[3] // mmin
                            if (cntlst[1] == 2 and cntlst[2] == 1 and cntlst[3] == 1) or (cntlst[1] == 1 and cntlst[2] == 1 and cntlst[3] == 2):
                                cntlst[0] = 3
                            elif (cntlst[1] == 2 and cntlst[2] == 2 and cntlst[3] == 1) or (cntlst[1] == 1 and cntlst[2] == 2 and cntlst[3] == 2):
                                cntlst[0] = 2
                            else:
                                cntlst[0] = 1
                            value[idx] = deco[cntlst[0]][cntlst[1]][cntlst[2]][cntlst[3]]
                            if sample != '0000':
                                x+=1
                            break

                        start = 3
                        pre = now

                a = value[0] + value[2] + value[4] + value[6]
                b = value[1] + value[3] + value[5] + value[7]
                value = [0] * 8
                idx = 7
                if (a*3 + b) % 10 == 0:
                    result += (a + b)

            x-=1
    return result

for tc in range(int(input())):
    N,M = map(int,input().split())
    data = [list(input()) for _ in range(N)]

    print("#{} {}".format(tc+1,func()))





