import sys
sys.stdin = open("2669.txt","r")

lst=[ [0]*100 for _ in range(100)]
check=[]
result=0

for i in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    check.append((x1,y1,x2,y2))

while check:
    x1,y1,x2,y2=check.pop()
    for y in range(y1,y2):
        for x in range(x1,x2):
            if lst[y][x]==0:
                result+=1
            lst[y][x]=1

print(result)
