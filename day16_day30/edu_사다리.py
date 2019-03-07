import sys
sys.stdin = open("사다리.txt","r")

def sol(start_x):
    global result
    ry,rx = -1,-1
    count = 0
    stack = [(0,start_x)]
    while stack:
        y,x = stack.pop(0)
        for i in range(3):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=nx<100 and 0<=ny<100 and data[ny][nx] and not (ny == ry and nx == rx) :
                stack.append((ny,nx))
                count+=1
                ry,rx = y,x
                break

    result.append((start_x,count))



MIS = lambda: map(int,input().split())
for tc in range(10):
    tr=input()
    data = [ list(MIS()) for _ in range(100) ]

    result = []
    #우좌하
    dx = [1, -1,0]
    dy = [0,0,1]

    for x in range(100):
        if data[0][x]:
            sol(x)
    result.sort(key=lambda x : x[1])
    list.sort
    print("#{} {}".format(tc+1,result[0][0]))
    # print("#{} {}".format(tc+1,result))

    # 1 18
    # 2 96
    # 3 16
    # 4 5
    # 5 99
    # 6 0
    # 7 97
    # 8 0
    # 9 62
    # 10 3
