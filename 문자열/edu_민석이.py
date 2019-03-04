import sys
sys.stdin = open("민석이.txt","r")

for tc in range(int(input())):
    n, k = map(int,input().split())
    result = [0 for _ in range(n)]
    for i in map(int,input().split()):
        result[i-1] += 1

    print("#{} ".format(tc+1),end="")
    for j in range(1,n+1):
        if not result[j-1]:
            print(j,end=" ")
    print()
