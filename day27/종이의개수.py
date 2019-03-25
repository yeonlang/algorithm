import sys
sys.stdin = open("종이의개수.txt")

def divcon(M,Y,X):
    for y in range(Y,Y+M):
        for x in range(X,X+M):
            if y == Y and x == X: continue
            if data[y][x] != data[Y][X]:
                divcon(M//3, Y, X)
                divcon(M//3, Y, X+M//3)
                divcon(M//3, Y, X+2*(M//3))
                divcon(M//3, Y+M//3, X)
                divcon(M//3, Y+M//3, X+M//3)
                divcon(M//3, Y+M//3, X+2*(M//3))
                divcon(M//3, Y+2*(M//3), X)
                divcon(M//3, Y+2*(M//3), X+M//3)
                divcon(M//3, Y+2*(M//3), X+2*(M//3))
                return
    result[data[Y][X]]+=1

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
result = [0,0,0]
divcon(N,0,0)
print(result[-1])
print(result[0])
print(result[1])
