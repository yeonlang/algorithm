import sys
sys.stdin = open("input2.txt","r")

Info = [-1] * 128 #char 1bite ASCII code 7bit
Data = input()

Info[ord(')')]='('
Info[ord(']')]='['
Info[ord('}')]='{'
Info[ord('>')]='<'

judge=[40, 60, 91, 123, 41, 62, 93, 125]
stack = [0]*10
top = -1

howmany=len(Data)
flag=True

for i in range(howmany):

    if ord(Data[i]) in judge[:4]:
        top += 1
        stack[top] = Data[i]

    elif Info[ord(Data[i])] == stack[top] :
        stack[top] = 0
        top -= 1

    elif ord(Data[i]) in judge[4:]:
        flag=False

if top == -1 and flag:
    print('통과')
else:
    print('오류')
