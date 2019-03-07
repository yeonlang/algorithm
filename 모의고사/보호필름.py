import sys
sys.stdin = open("보호필름.txt","r")

from itertools import combinations,product

def func():
    for x in range(M):
        flag = False
        for y in range(N-K+1):
            count = 0
            for k in range(K):
                if data[y+k][x]:
                    count+=1
            if count > K:
                flag = True
                break
        if flag:
            continue
        else:
            break
    if flag:
        return 1
    else:
        for x in range(M):
            flag = False
            for y in range(N - K + 1):
                count = 0
                for k in range(K):
                    if data[y + k][x] == 0:
                        count += 1
                if count > K:
                    flag = False
                    break
            if flag:
                continue
            else:
                return 0
        return 1

def sol():
    t = 1
    while t != K:
        for i in combinations(range(N), t):
            temp = [0]*N
            for j in i:
                temp[j] = data[j]

            for loca,value in product([i], set(combinations([1, 0]*t, t))):

        t+=1
    return 0


for tc in range(int(input())):
    N,M,K = map(int,input().split())
    data = [ list(map(int,input().split())) for _ in range(N) ]

    print(sol())

#1 2
#2 0
#3 4
#4 2
#5 2
#6 0
#7 3
#8 2
#9 3
#10 4

