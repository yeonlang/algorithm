import sys
sys.stdin = open("비트마스크ex1.txt","r")

lst = []
for p in input().split():
    lst+=list(map(int,p))

result = 0

# for i in range(len(lst)):
#     temp = (1<<6)>>(i%7)
#
#     if temp&(lst[i]<<6)>>(i%7):
#         result+=temp
#
#     if i%7==6:
#         print(result)
#         result = 0

t = 0

for i in range(len(lst)):
    t = t*2 + int(lst[i])
    if (i+1)%7 == 0:
        print(t)
        t = 0
