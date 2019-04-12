import sys
sys.stdin = open("원자소멸.txt")

from collections import defaultdict
class Atom:
    def __init__(self,x,y,d,power):
        self.x = x
        self.y = y
        self.d = d
        self.power = power

dy = [1,-1,0,0]
dx = [0,0,-1,1]
for tc in range(int(input())):
    minx,miny = 1000,1000
    maxx,maxy = -1000,-1000
    K = int(input())
    data = []
    for _ in range(K):
        x,y,d,power = map(int,input().split())
        minx = min(x,minx)
        miny = min(y,miny)
        maxx = max(x,maxx)
        maxy = max(y,maxy)
        data.append(Atom(x,y,d,power))

    N = (maxy-miny)*2
    M = (maxx-minx)*2

    for i in range(K):
        atom = data[i]
        atom.x-=minx
        atom.x *= 2
        atom.y-=miny
        atom.y *= 2

    count = 0
    stack = []
    while data:
        Atom.visited = defaultdict(lambda:0)
        i = 0
        while i<len(data):
            atom = data[i]
            atom.y += dy[atom.d]
            atom.x += dx[atom.d]
            if atom.x>M or atom.x<0 or atom.y>N or atom.y<0:
                data.pop(i)
                continue
            if Atom.visited[(atom.y,atom.x)]:
                count += atom.power
                stack.append((atom.y,atom.x))
                data.pop(i)
                continue
            Atom.visited[(atom.y,atom.x)] = 1
            i+=1

        while stack:
            y,x = stack.pop()
            for t in range(len(data)):
                atom = data[t]
                if atom.y == y and atom.x == x:
                    count += atom.power
                    data.pop(t)
                    break

    print('#{} {}'.format(tc+1,count))




