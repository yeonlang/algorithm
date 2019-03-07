import sys
sys.stdin = open("14696.txt","r")

for tc in range(int(input())):

    A_lst = list(map(int,input().split()))[1:]
    B_lst = list(map(int, input().split()))[1:]

    judge = [0, 0, 0, 0]

    for i in range(len(A_lst)):
        judge[A_lst[i]-1]+=1
    for j in range(len(B_lst)):
        judge[B_lst[j]-1]-=1

    for k in range(3,-1,-1):
        if judge[k]>0:
            print('A')
            break
        elif judge[k]<0:
            print('B')
            break
    else :
        print('D')