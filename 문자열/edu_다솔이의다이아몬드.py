import sys
sys.stdin = open("다솔이의다이아몬드.txt","r")

def dfs(y,x):
    for nxt in range(8):
        ny = y+dy[nxt]
        nx = x+dx[nxt]
        if 0<=ny<5 and 0<=nx<x_length and result[ny][nx] == '.':
            result[ny][nx] = '#'

for tc in range(int(input())):
    data = input()
    n = len(data)
    x_length = 4*n+1
    result = [ ['.']*x_length for _ in range(5) ]
    for i in range(n):
        result[2][4*i+2] = data[i]

    dx = [-2,2,-1,1,0,0,-1,1]
    dy = [0,0,-1,-1,-2,2,1,1]

    for y in range(5):
        for x in range(x_length):
            if result[y][x] != '.' and result[y][x] != '#':
                dfs(y,x)

    for y in range(5):
        for x in range(x_length):
            print(result[y][x],end="")
        print()


