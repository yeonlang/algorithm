import sys
sys.stdin = open("회문.txt","r")


for tc in range(int(input())):
    n, m = map(int,input().split())
    data = [input() for _ in range(n)]

    flag = False
    result = ''

    # 가로 탐색
    for y in range(n):
        for x in range(n-m+1):
            k = 0
            while True:
                if data[y][x+k] == data[y][m+x-(k+1)]:
                    if k == m-1:
                        result = data[y][x:x+m]
                        flag = True
                        break
                    k += 1
                else:
                    break

    #세로탐색
    if not flag:
        for y in range(n):
            for x in range(n-m+1):
                k = 0
                while True:
                    if data[x+k][y] == data[m+x-(k+1)][y]:
                        if k == m-1:
                            for t in range(x,x+m):
                                result+=data[t][y]
                            break
                        k += 1
                    else:
                        break

    print("#{0} {1}".format(tc+1,result))

