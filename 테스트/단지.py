import sys
sys.stdin = open("단지.txt")

N = int(input())
data = [list(map(int,input())) for _ in range(N)]
visited=[[0]*N for _ in range(N)]

BTK(0,0)
