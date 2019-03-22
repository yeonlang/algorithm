import sys
sys.stdin = open("활주로.txt")

def IsCanFly(arr):
    cnt1 = [0]*N
    for i in range(N):
        if 0<arr[i]<=K:
            cnt1[arr[i]]+=1

    for j in range(2,K+1):
        if cnt1[j]==cnt1[j-1]:
            continue
        else:
            return False
    return True

def IsPass(arr1,arr2):
    for i in range(N):
        if 0<arr1[i]<=K and 0<arr2[i]<=K:
            return False
    return True

def readX():
    global result
    for x in range(N):
        flag1,flag2 = True,True
        cntr = [0] * N
        cntl = [0] * N
        cnt = [0] * N

        for y in range(1,N):
            if abs(data[y-1][x] - data[y][x]) > 1:
                flag1 = False
                break
            elif data[y-1][x] - data[y][x] == 1:
                cntr[y] = 1
            elif data[y-1][x] == data[y][x] and cntr[y-1]:
                cntr[y] = cntr[y-1]+1

        for y in range(N-2,-1,-1):
            if abs(data[y+1][x] - data[y][x]) > 1:
                flag1 = False
                break
            elif data[y+1][x] - data[y][x] == 1:
                cntl[y] = 1
            elif data[y+1][x] == data[y][x] and cntl[y+1]:
                cntl[y] = cntl[y+1] + 1
        if not flag1: continue

        if IsCanFly(cntl) and IsCanFly(cntr) and IsPass(cntl,cntr):
            for i in range(N):
                if 0<cntl[i]<=K:
                    cnt[cntl[i]]+=1
                if 0<cntr[i]<=K:
                    cnt[cntr[i]]+=1
            for j in range(2,K):
                if cnt[j]==cnt[j-1]:
                    continue
                else:
                    flag2 = False
            if flag2:
                result+=1

def readY():
    global result
    for y in range(N):
        flag1,flag2 = True,True
        cntr = [0] * N
        cntl = [0] * N
        cnt = [0] * N

        for x in range(1,N):
            if abs(data[y][x-1] - data[y][x]) > 1:
                flag1 = False
                break
            elif data[y][x-1] - data[y][x] == 1:
                cntr[x] = 1
            elif data[y][x-1] == data[y][x] and cntr[x-1]:
                cntr[x] = cntr[x-1]+1

        for x in range(N-2,-1,-1):
            if abs(data[y][x+1] - data[y][x]) > 1:
                flag1 = False
                break
            elif data[y][x+1] - data[y][x] == 1:
                cntl[x] = 1
            elif data[y][x+1] == data[y][x] and cntl[x+1]:
                cntl[x] = cntl[x+1] + 1
        if not flag1: continue

        if IsCanFly(cntl) and IsCanFly(cntr) and IsPass(cntl,cntr):
            for i in range(N):
                if 0<cntl[i]<=K:
                    cnt[cntl[i]]+=1
                if 0<cntr[i]<=K:
                    cnt[cntr[i]]+=1
            for j in range(2,K):
                if cnt[j]==cnt[j-1]:
                    continue
                else:
                    flag2 = False
            if flag2:
                result+=1


for tc in range(int(input())):
    N, K = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    readY()
    readX()
    print("#{} {}".format(tc+1,result))


