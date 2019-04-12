import sys
sys.stdin = open("최대상금.txt")

def BTK(c,idx,data,num,di):
    global myMax,myMaxlst
    if c == 2:
        copydata = data[:]
        copydata[di[0]],copydata[di[1]] = copydata[di[1]],copydata[di[0]]
        if num == N:
            cnt = 0
            t = 1
            for i in range(l-1,-1,-1):
                cnt+=copydata[i]*t
                t = t*10
            if cnt>myMax:
                myMax = cnt
                myMaxlst = copydata[:]
        else:
            BTK(0,0,copydata,num+1,[0,0])
        return

    if myMaxlst[0]>data[0] and c == 1 and idx > 1: return
    for i in range(idx,l):
        di[c] = i
        BTK(c+1,i+1,data,num,di)
        di[c] = 0


for tc in range(int(input())):
    data, N = input().split()
    N = int(N)
    data = list(map(int,data))
    l = len(data)
    if N>l:
        data.sort(reverse=True)
        copydata = data[:]
        copydata[-1],copydata[-2] = copydata[-2],copydata[-1]
        cnt = 0
        t = 1
        for i in range(l-1,-1,-1):
            cnt+=data[i]*t
            t= t*10
        sum1 = cnt
        cnt = 0
        t = 1
        for i in range(l-1, -1, -1):
            cnt += copydata[i]*t
            t = t*10
        sum2 = cnt
        if (not N%2 and not l%2) or (l%2 and N%2):
            print("#{} {}".format(tc+1, sum2))
            continue
        else:
            print("#{} {}".format(tc+1, sum1))
            continue

    myMax = 0
    myMaxlst = [0]*l
    BTK(0, 0, data, 1, [0, 0])
    print("#{} {}".format(tc+1,myMax))

#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645

