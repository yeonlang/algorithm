import sys
sys.stdin = open("소방차.txt","r")

data=[0]*100

p,f = map(int,input().split())
pumps = list(map(int,input().split()))
cars = list(map(int,input().split()))

for i in range(p):
    data[pumps[i]]=1
for j in range(f):
    if data[cars[j]] == 1:
        data[cars[j]]=0
        continue
    data[cars[j]]=2

print(data)





