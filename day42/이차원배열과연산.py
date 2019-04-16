import sys
sys.stdin = open("이차원배열과연산.txt")

def count(flag):
    global c_maxlen,r_maxlen
    if flag:
        nxtc_len = c_maxlen
        for y in range(r_maxlen):
            for x in range(c_maxlen):
                if data[y][x]:
                    cnt[data[y][x]]+=1

            cnt[0] = 0
            tp = []
            for num in range(1,101):
                if cnt[num]:
                    val,cnt[num] = cnt[num],0
                    tp.append((num,val))
            tp.sort(key=lambda x: (x[1],x[0]))
            if len(tp)>50:
                tp = tp[:51]
            for i in range(len(tp)):
                a,b = tp[i][0],tp[i][1]
                data[y][i*2] = a
                data[y][i*2+1] = b

            if len(tp)*2 < c_maxlen:
                for j in range(len(tp)*2,c_maxlen):
                    data[y][j] = 0

            if len(tp)*2 > nxtc_len:
                nxtc_len = len(tp)*2
        c_maxlen = nxtc_len

    else:
        nxtr_len = r_maxlen
        for x in range(c_maxlen):
            for y in range(r_maxlen):
                if data[y][x]:
                    cnt[data[y][x]] += 1

            cnt[0] = 0
            tp = []
            for num in range(1,101):
                if cnt[num]:
                    val,cnt[num] = cnt[num],0
                    tp.append((num,val))
            tp.sort(key=lambda x: (x[1],x[0]))

            if len(tp)>50:
                tp = tp[:51]

            for i in range(len(tp)):
                a,b = tp[i][0],tp[i][1]
                data[i*2][x] = a
                data[i*2+1][x] = b

            if len(tp)*2 < r_maxlen:
                for j in range(len(tp)*2,r_maxlen):
                    data[j][x] = 0

            if len(tp)*2>nxtr_len:
                nxtr_len = len(tp)*2
        r_maxlen = nxtr_len

cnt = [0]*101
r,c,K = map(int,input().split())
r,c = r-1,c-1
data = [[0]*100 for _ in range(100)]

for y in range(3):
    for x,val in enumerate(map(int,input().split())):
        data[y][x] = val
r_maxlen = 3
c_maxlen = 3

time = 0
while data[r][c] != K and time<=100:
    if r_maxlen>=c_maxlen:
        flag = 1
    else:
        flag = 0
    count(flag)
    time+=1
if time != 101:
    print(time)
else:
    print(-1)
