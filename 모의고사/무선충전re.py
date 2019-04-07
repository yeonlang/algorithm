import sys
sys.stdin = open("무선충전.txt")



for tc in range(int(input())):
    T, N = map(int,input().split())
    dirA = list(map(int,input().split()))
    dirB = list(map(int,input().split()))

    charger = []
    for _ in range(N):
        x,y,c,p = map(int,input().split())
        x-=1
        y-=1
        charger.append((y,x,c,p))






