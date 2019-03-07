import sys
sys.stdin = open("스위치켜고끄기.txt","r")

def male(index):
    for i in range(index,n+1,index):
        data[i] = 1

def female(index):
    i=0

    while 0<=index-i and index+i<n and data[index-i] == data[index+i]:
        if i == 0:
            data[index] = 0 if data[index] else 1
        else:
            data[index-i] = 0 if data[index-i] else 1
            data[index+i] = 0 if data[index+i] else 1
        i+=1


n=int(input())
data = list(map(int,input().split()))
# print(data)

for tc in range(int(input())):
    s,index = map(int,input().split())
    if s == 1:
        male(index)
        print(data)

    if s == 2:
        female(index)
        print(data)

print(*data)


