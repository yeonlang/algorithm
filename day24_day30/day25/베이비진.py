import sys
sys.stdin = open("베이비진.txt")

def read(data):
    for i in range(1,len(data)-1):
        if data[i-1] and data[i] and data[i+1]:
            return True
        if data[i-1] == 3:
            return True
    if data[-1] == 3 or data[-2] == 3:
        return True

for tc in range(int(input())):
    cntA = [0]*12
    cntB = [0]*12
    result = 0
    for i,value in enumerate(map(int,input().split())):
        if not i&1:
            cntA[value]+=1
            if read(cntA):
                result = 1
                break
        else:
            cntB[value] += 1
            if read(cntB):
                result = 2
                break

    print("#{} {}".format(tc+1,result))
