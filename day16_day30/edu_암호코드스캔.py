import sys
sys.stdin = open("암호코드스캔.txt","r")



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


    for y in range(H):
        temp = list(input())
        x = len(temp)-1
        while x != 0:
            if temp[x] != '0':
                t = x
                while temp[t] != '0':
                    t-=1
                dataset.add(tuple(temp[t+1:x+1]))
                x=t
                continue
            x-=1

    for indata in dataset:
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
        n_lst=[]
        tn=1
        while tn*56<=len(data):
            n_lst.append(tn)
            tn+=1

        for n in n_lst:

            while start<len(data)-(56*n):
                result = []
                temp = [1] * (7*n)
                flag = True
                for now in range(start+1,start+(56*n)):
                    temp[0] = 1
                    temp[now%(7*n)] = temp[now%(7*n)-1]+1 if data[now] == data[now-1] else 1

                    if now%(7*n) == (7*n)-1:
                        decoin = [0]*4
                        d=0
                        for idx_t in range(7*n-1):
                            if temp[idx_t]>=temp[idx_t+1]:
                                decoin[d]=temp[idx_t]
                                d+=1
                        decoin[d] = temp[-1]
                        jud = deco[decoin[0]//n][decoin[1]//n][decoin[2]//n][decoin[3]//n]
                        if jud == -1:
                            flag = False
                            break
                        result.append(jud)
                if flag:
                    temp2=0
                    for idx_r in range(len(result)):
                        if idx_r&1:
                            temp2+=result[idx_r]
                        else:
                            temp2+=result[idx_r]*3
                    if temp2%10 == 0:
                        print("#{} {}".format(tc+1,sum(result)))
                else:
                    start += 1







