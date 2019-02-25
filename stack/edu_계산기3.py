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
    #')'
    isp[41] = 0
    icp[41] = 0
    #'('
    isp[40] = 0
    icp[40] = 3
    #'+' '-'
    #'*' '/'
    icp[43] = icp[45] = isp[43] = isp[45] = 1
    icp[47] = icp[42] = isp[47] = isp[42] = 2

    stack = [0]*100
    result=[]
    top = -1

    n=int(input())
    data = input()

    for i in range(len(data)):
        value=data[i]
        if ord(value) == 40:
            push(data[i])
            continue

        # ')'
        if value == ')':
            while True:
                judge=pop()
                if judge == '(':
                    break
                else:
                    result.append(judge)
                    if not stack:
                        break
            continue

        if isp[ord(value)] == -1:
            result.append(value)

        else:
            while icp[ord(value)] < isp[ord(stack[top])]:
                temp=pop()
                result.append(temp)
            push(value)


    while top>=0:
        result.append(pop())
    print(*result)
    while len(result)>1:
        for i in range(len(result)):
            if result[i] == '+' or result[i] == '-' or result[i] == '/' or result[i] == '*':
                temp=my_math(int(result[i-1]), int(result[i-2]), ord(result[i]))
                del result[i - 2:i]
                result[i-2] = temp
                break

    print(f"#{tc+1} {result[0]}")






