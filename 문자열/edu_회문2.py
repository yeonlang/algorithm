import sys
sys.stdin = open("회문2.txt","r")

def search(flag):
    for m in range(100, 0, -1):
        for y in range(100):
            for x in range(100 - m + 1):
                k = 0
                while True:
                    if flag == '가로':
                        if data[y][x + k] == data[y][m + x - (k + 1)]:
                            if k == m - 1:
                                return m
                            k += 1
                        else:
                            break
                    if flag == '세로':
                        if data[x + k][y] == data[m + x - (k + 1)][y]:
                            if k == m - 1:
                                return m
                            k += 1
                        else:
                            break

for tc in range(10):
    num = int(input())
    data = [ input() for _ in range(100) ]

    result = max(search('가로'),search('세로'))
    print("#{} {}".format(tc+1,result))

#1 18
#2 17
#3 17
#4 20
#5 18
#6 21
#7 18
#8 18
#9 17
#10 18
