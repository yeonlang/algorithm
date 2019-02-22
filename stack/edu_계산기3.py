import sys
sys.stdin = open("계산기3.txt","r")

def my_math(num1 ,num2 ,op):
    if op == 42:
        return num2 * num1
    elif op == 43:
        return num2 + num1
    elif op == 45:
        return num2 - num1
    elif op == 47:
        return num2 // num1
    return

def push(x):
    global stack, top
    top+=1
    stack[top]=x

def pop():
    global stack, top
    if top == -1:
        return False
    value=stack[top]
    stack[top]=0
    top-=1
    return value

for tc in range(10):
    icp = [-1] * 128
    isp = [-1] * 128
    isp[41] = 3
    icp[41] = 0
    isp[40] = 0
    icp[40] = 4
    icp[43] = icp[45] = isp[43] = isp[45] = 1
    icp[47] = icp[42] = isp[47] = isp[42] = 2

    stack = [0]*100
    result=[]
    top = -1

    n=int(input())
    data = input()

    for i in range(len(data)):
        value=data[i]
        if ord(data[i]) == 40:
            push(data[i])
            continue
        if ord(data[i]) == 41:
            flag=''
            while flag!='(':
                flag=pop()
                result.append(flag)
            result.pop()
            continue

        if isp[ord(data[i])] == -1:
            result.append(data[i])
            continue
        what=stack[top]
        if top == -1 or icp[ord(data[i])] >= isp[ord(stack[top])]:
            push(data[i])
        else:
            while icp[ord(data[i])] < isp[ord(stack[top])]:
                result.append(pop())
            result.append(data[i])
    while top>=0:
        result.append(pop())

    print(result)
    # while len(result)>1:
    #     for i in range(len(result)):
    #         if result[i] == '+' or result[i] == '-' or result[i] == '/' or result[i] == '*':
    #             temp=my_math(int(result[i-1]), int(result[i-2]), ord(result[i]))
    #             del result[i - 2:i]
    #             result[i-2] = temp
    #             break
    #
    # print(f"#{tc+1} {result[0]}")






