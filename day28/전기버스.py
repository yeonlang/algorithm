import sys
sys.stdin = open("전기버스.txt")

def DFS(c,idx,power):
    global myMin
    if idx+power-1 >= N-1:
        if c<myMin:
            myMin = c
            return
    if c>=myMin: return
    for i in range(idx,idx+power):
        DFS(c+1,i+1,data[i])

for tc in range(int(input())):
    for i,value in enumerate(map(int,input().split())):
        if i == 0:
            N = value
            data = [0]*N
            continue
        data[i-1] = value
    myMin = 987654321
    DFS(0,1,data[0])
    print(myMin)

#1 1
#2 2
#3 5
#4 2
#5 4
#6 6
#7 11
#8 10
#9 8
#10 7