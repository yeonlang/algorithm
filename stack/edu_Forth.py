import sys
sys.stdin = open("Forth.txt","r")

def f(s):
    if len(s)>1:
        return int(s)
    elif 48<=ord(s)<=57:
        return int(s)
    else :
        return s

def my_math(num1,num2,op):
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
    global stack, top, result
    if top == -1:
        result = False
        return
    data=stack[top]
    stack[top]=0
    top-=1
    return data

for tc in range(int(input())):
    stack = [0] * 257
    top = -1
    judge = [43, 45, 47, 42]
    result = True
    my_str = list(map(f, input().split()))

    for i in range(len(my_str)):
        if type(my_str[i]) == int:
            push(my_str[i])

        elif ord(my_str[i]) in judge :
            a=pop()
            b=pop()
            if a and b:
                push(my_math(a,b,ord(my_str[i])))
                continue
            else:
                result=False
                continue
        elif ord(my_str[i]) == 46:
            if result and top == 0:
                pr=pop()
                print(f'#{tc+1} {pr}')
            else:
                print(f'#{tc+1} error')







