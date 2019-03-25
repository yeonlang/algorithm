import sys
sys.stdin = open("2263.txt")

def divcon(left,root,right):
    global result
    result += root+' '
    if len(left) == 1:
        result += left[0]+' '
    elif left:
        l = len(left)//2
        divcon(left[:l],left[l],left[l+1:])

    if len(right) == 1:
        result += right[0]+' '
    elif right:
        r = len(right)//2
        divcon(right[:r],right[r],right[r+1:])

result = ''
N = int(input())
data1 = list(input().split())
data2 = list(input().split())
root = data2[-1]
for i in range(N):
    if data1[i] == root:
        divcon(data1[:i],data1[i],data1[i+1:])
        break
print(result)

#3 1 2 4 5 3 6 7
