import sys
sys.stdin = open('practice01.txt', 'r')

def IsSafe(y,x):
    if x>=0 and x<5 and y>=0 and y<5:
        return True
    else:
        return False

def Mycalc(a,b):
    if a>b :
        return a-b
    else :
        return b-a

lst = [ 0 for _ in range(5) ]

for _ in range(5):
    lst[_] = list(map(int, input().split()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

sum = 0
for y in range(5):
    for x in range(5):
        for dir in range(4):
            newX = x + dx[dir]
            newY = y + dy[dir]
            if IsSafe(newY,newX):
                sum += Mycalc(lst[y][x], lst[newY][newX])
print(sum)