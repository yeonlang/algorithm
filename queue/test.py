import sys
sys.stdin=open("input.txt","r")


result=[]
result+=list(map(int,input().split()))
result+=list(map(int,input().split()))
result.sort()
print(result)