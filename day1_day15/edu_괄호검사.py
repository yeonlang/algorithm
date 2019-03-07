import sys
sys.stdin = open("input2.txt","r")

for tc in range(int(input())):
    Info = [-1] * 128  # char 1bite ASCII code 7bit
    Info[ord(')')] = '('
    Info[ord('}')] = '{'

    judge = [40, 123, 41, 125]
    stack = [0] * 1000
    top = -1

    Data=input()
    howmany=len(Data)
    flag=True

    for i in range(howmany):

        if ord(Data[i]) in judge[:2]:
            top += 1
            stack[top] = Data[i]

        elif Info[ord(Data[i])] == stack[top] :
            stack[top] = 0
            top -= 1

        elif ord(Data[i]) in judge[2:]:
            flag=False

    if top == -1 and flag:
        print(f'#{tc+1} {1}')
    else:
        print(f'#{tc+1} {0}')
