import sys
sys.stdin = open("단어어디.txt","r")

def sol(start_y,start_x,k):
    global result
    for i in range(2):
        visited = [[0] * n for _ in range(n)]
        visited[start_y][start_x] = 1
        count = 1
        stack = [(start_y,start_x)]
        while stack:
            y,x = stack.pop(0)
            for j in range(2):
                ny = y + dy[i][j]
                nx = x + dx[i][j]
                if 0<=nx<n and 0<=ny<n and data[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    stack.append((ny,nx))
                    count+=1
        if count == k:
            result += 1

MIS = lambda: map(int,input().split())
for tc in range(int(input())):
    n,k = MIS()
    data = [ list(MIS()) for _ in range(n) ]

    result = 0

    dx = [[1, -1],[0, 0]]
    dy = [[0, 0],[1, -1]]

    for y in range(n):
        for x in range(n):
            if data[y][x]:
                sol(y,x,k)
    print("#{} {}".format(tc+1,result // k))

    # 1 2
    # 2 6
    # 3 6
    # 4 0
    # 5 14
    # 6 2
    # 7 45
    # 8 0
    # 9 98
    # 10 7


