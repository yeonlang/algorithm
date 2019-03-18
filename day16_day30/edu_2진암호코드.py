import sys
sys.stdin = open("2진암호코드.txt","r")



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
    result = []

    flag = True
    for h in range(H):
        temp = list(map(int,input()))
        if flag:
            for i in range(len(temp)-1,-1,-1):
                if temp[i] and flag:
                    data = temp[i-55:i+1]
                    flag = False

    temp = [1] * 7
    for now in range(1,56):
        temp[now%7] = temp[now%7-1]+1 if data[now] == data[now-1] else 1

        if now%7 == 6:
            decoin = [0]*4
            d=0
            for idx_t in range(6):
                if temp[idx_t]>=temp[idx_t+1]:
                    decoin[d]=temp[idx_t]
                    d+=1
            decoin[d] = temp[-1]
            result.append(deco[decoin[0]][decoin[1]][decoin[2]][decoin[3]])

    temp2=0
    for idx_r in range(len(result)):
        if idx_r&1:
            temp2+=result[idx_r]
        else:
            temp2+=result[idx_r]*3
    if temp2%10:
        print("#{} {}".format(tc+1,0))
    else:
        print("#{} {}".format(tc+1,sum(result)))


#1 38
#2 0
#3 34
#4 28
#5 24
#6 26
#7 36
#8 30
#9 0
#10 34






