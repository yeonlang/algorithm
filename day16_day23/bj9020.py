import sys
sys.stdin = open("bj9020.txt","r")

def sol():
    while True:
        for a in range(N // 2):
            for b in range(N // 2):
                if newdata[start+a] + newdata[start-b] == N:
                    print(newdata[start-b], newdata[start+a])
                    return

data = [i if i > 1 else 0 for i in range(10001)]

for i in range(2, 10001):
    if data[i] != 0:
        n = 2
        while i * n < len(data):
            data[i * n] = 0
            n += 1
newdata=set(data)
newdata.remove(0)
newdata = list(newdata)
newdata.sort()
l = len(newdata)

for tc in range(int(input())):
    N =int(input())
    if N//2 in newdata:
        print(N//2,N//2)
    else:
        for j in range(l):
            if N//2 < newdata[j]:
                start =j
                break
    sol()



