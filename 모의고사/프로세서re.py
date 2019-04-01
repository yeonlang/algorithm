import sys
sys.stdin = open("엑시노스.txt")

from collections import defaultdict
def func(y,x,d):
    s = set()
    while True:
        y+=dy[d]
        x+=dx[d]
        if data[y][x]:
            return False
        s.add((y,x))
        if y == N-1 or x == N-1 or y == 0 or x == 0:
            return s

def BTK(c):
    global maxchoice, minlength

    if c>maxchoice:


dy = [-1,0,1,0]
dx = [0,1,0,-1]

for tc in range(int(input())):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]

    core = defaultdict(lambda : [])
    for y in range(1,N-1):
        for x in range(1,N-1):
            if data[y][x]:
                for d in range(4):
                    temp = func(y,x,d)
                    if temp:
                        core[(y,x)].append(temp)
    maxchoice = 0
    minlength = 987654321

