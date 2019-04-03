def BTK(c,cnt):
    global myMin
    if c == N:
        if cnt<myMin:
            myMin = cnt
        return

    if cnt>=myMin:
        return

    for i in range(N):
        if not i in visited:
            visited.append(i)
            fy, fx = chip[i][0], chip[i][1]
            y, x = robot[c][0], robot[c][1]
            nxtcnt = cnt + abs(y - fy) + abs(x - fx)
            BTK(c+1,nxtcnt)
            visited.pop()

for tc in range(int(input())):
    N = int(input())
    C = list(map(int,input().split()))
    R = list(map(int,input().split()))
    chip = []
    robot = []
    visited = []
    for i in range(N):
        y = C[2*i]
        x = C[2*i+1]
        chip.append((y,x))
    for i in range(N):
        y = R[2*i]
        x = R[2*i+1]
        robot.append((y,x))
    myMin = 987654321
    BTK(0,0)
    print("#{} {}".format(tc+1,myMin))




